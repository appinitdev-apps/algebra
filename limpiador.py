import os
import re
import argparse
from pathlib import Path


# ============================================================
# CONFIGURACIÓN
# ============================================================

EXCLUDED_DIRS = {
    ".git",
    ".idea",
    ".vscode",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "env",
    "build",
    "dist",
}

TARGET_EXTENSIONS = {
    ".md",
    ".readme",
    ".markdown",
}


# ============================================================
# LIMPIEZA DE ARCHIVOS .BAK EXISTENTES
# ============================================================

def remove_existing_backups(root, dry_run=False):
    root = Path(root)
    deleted_count = 0

    for current_root, dirs, files in os.walk(root):
        dirs[:] = [
            d for d in dirs
            if d.lower() not in {x.lower() for x in EXCLUDED_DIRS}
        ]

        for filename in files:
            if filename.lower().endswith(".bak"):
                bak_path = Path(current_root) / filename
                try:
                    rel = bak_path.relative_to(root)
                except ValueError:
                    rel = bak_path

                if dry_run:
                    print(f"   🗑 [DRY-RUN] Se eliminaría backup: {rel}")
                else:
                    try:
                        bak_path.unlink()
                        print(f"   🗑️ Backup eliminado: {rel}")
                        deleted_count += 1
                    except Exception as error:
                        print(f"   ❌ Error al eliminar {rel}: {error}")

    return deleted_count


# ============================================================
# BUSCAR ARCHIVOS RECURSIVAMENTE
# ============================================================

def is_target_file(filename: str) -> bool:
    name_lower = filename.lower()

    if name_lower.endswith(".bak"):
        return False

    if name_lower == "readme":
        return True

    path_obj = Path(filename)
    if path_obj.suffix.lower() in TARGET_EXTENSIONS:
        return True

    return False


def find_markdown_files(root):
    root = Path(root)

    for current_root, dirs, files in os.walk(root):
        dirs[:] = [
            d for d in dirs
            if d.lower() not in {x.lower() for x in EXCLUDED_DIRS}
        ]

        for filename in files:
            if is_target_file(filename):
                yield Path(current_root) / filename


# ============================================================
# PROTEGER BLOQUES DE CÓDIGO
# ============================================================

def protect_code_blocks(text):
    blocks = []
    pattern = re.compile(r"(```[\s\S]*?```|~~~[\s\S]*?~~~)")

    def replace(match):
        index = len(blocks)
        blocks.append(match.group(0))
        return f"@@@CODE_BLOCK_{index}@@@"

    text = pattern.sub(replace, text)
    return text, blocks


def restore_code_blocks(text, blocks):
    for index, block in enumerate(blocks):
        placeholder = f"@@@CODE_BLOCK_{index}@@@"
        text = text.replace(placeholder, block)
    return text


# ============================================================
# SANEAMIENTO Y LIMPIEZA DE LATEX / KATEX
# ============================================================

def fix_latex_syntax(text):
    """
    Corrige incompatibilidades de LaTeX en Markdown/KaTeX:
    1. Normaliza espacios indivisibles (NBSP).
    2. Arregla corchetes huérfanos que confunden al parser de Markdown.
    3. Asegura 4 barras invertidas antes de \\hline (evita 'Misplaced \\hline' y 'hline1').
    4. Corrige saltos de línea pegados directamente a llaves: '\\{\\' -> '\\\\ \\{\\'.
    5. Corrige llaves de conjuntos mal escapadas '{\\ ' a '\\{\\ '.
    6. Corrige saltos de línea rotos con espacios intermedios '\\ \\'.
    7. Elimina saltos con espaciado vertical incompatible: \\\\[...pt] -> \\\\.
    8. Reemplaza \\operatorname{...} por \\text{...}.
    9. Convierte \\begin{align} a \\begin{aligned} dentro de $$...$$.
    10. Elimina etiquetas \\tag{...} que provocan colapso vertical en flexbox.
    """
    # 1. Normalizar espacios indivisibles (NBSP \u00a0)
    text = text.replace("\u00a0", " ")

    # 2. Corregir corchetes de apertura huérfanos antes de palabras
    text = re.sub(r"\[(?=[a-zA-ZáéíóúÁÉÍÓÚ]+,?\s+)", "", text)

    # 3. Sanitizar interior de expresiones matemáticas ($...$ y $$...$$)
    def clean_math_content(match):
        math_content = match.group(0)

        # Separa saltos de línea pegados a una llave: '\\{\\' o '\\{' -> '\\\\ \n\\{' o '\\\\ \n{'
        math_content = re.sub(r"\\{2,4}(?=\\?\{)", r"\\\\ \n", math_content)

        # Corrige llaves de conjuntos mal escapadas: '{\ ' -> '\{\ '
        math_content = re.sub(r"\{(?=\\\s)", r"\\{", math_content)

        # Asegura 4 barras invertidas antes de \hline (escapado correcto para Markdown -> KaTeX)
        math_content = re.sub(r"\\{1,4}\s*\\?hline", r"\\\\\\\\ \\hline", math_content)

        # Corrige saltos de línea rotos con espacio intermedio '\ \' a '\\'
        math_content = re.sub(r"\\(?:\s+\\)+", r"\\\\", math_content)

        # Elimina \\[6pt], \\\\[10pt], etc.
        math_content = re.sub(r"(\\{1,4})\[\s*\d+\s*(?:pt|ex|em|px|mm|cm)?\s*\]", r"\1", math_content)

        # Sustituye \\operatorname{algo} por \\text{algo}
        math_content = re.sub(r"\\operatorname\{([^}]+)\}", r"\\text{\1}", math_content)

        # Sustituye entornos align por aligned dentro de los delimitadores $$...$$
        math_content = re.sub(r"\\begin\{align\}", r"\\begin{aligned}", math_content)
        math_content = re.sub(r"\\end\{align\}", r"\\end{aligned}", math_content)

        # Elimina \tag{...} para evitar el colapso a columna vertical
        math_content = re.sub(r"\\tag\{[^}]*\}", "", math_content)

        return math_content

    math_pattern = re.compile(r"(\$\$[\s\S]*?\$\$|\$(?!\$)[^\n$]+?\$(?!\$))")
    text = math_pattern.sub(clean_math_content, text)

    return text


# ============================================================
# ELIMINAR YAML FRONT MATTER
# ============================================================

def remove_yaml_front_matter(text):
    text = text.lstrip("\ufeff")

    lines = text.splitlines(keepends=True)
    if not lines:
        return text

    if lines[0].strip() != "---":
        return text

    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            text = "".join(lines[i + 1:])
            return text.lstrip("\r\n")

    return text


# ============================================================
# ELIMINAR ENLACES (INTERNOS Y EXTERNOS)
# ============================================================

def remove_all_links(text):
    text, blocks = protect_code_blocks(text)

    pattern = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")

    def replace(match):
        label = match.group(1).strip()
        destination = match.group(2).strip()

        dest_clean = re.split(r'\s+["\']', destination, maxsplit=1)[0].strip()

        if dest_clean.startswith("#"):
            return match.group(0)

        return label

    text = pattern.sub(replace, text)
    text = restore_code_blocks(text, blocks)
    return text


# ============================================================
# CENTRAR IMÁGENES
# ============================================================

def center_images(text):
    text, blocks = protect_code_blocks(text)
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

    def replace(match):
        alt = match.group(1).strip()
        destination = match.group(2).strip()

        title_match = re.match(r'(.+?)\s+["\'](.*?)["\']$', destination)

        if title_match:
            src = title_match.group(1).strip()
            title = title_match.group(2).strip()
            return (
                '<p align="center">\n'
                f'  <img src="{src}" alt="{alt}" title="{title}">\n'
                '</p>'
            )

        src = destination
        return (
            '<p align="center">\n'
            f'  <img src="{src}" alt="{alt}">\n'
            '</p>'
        )

    text = pattern.sub(replace, text)
    text = restore_code_blocks(text, blocks)
    return text


# ============================================================
# PROCESAR CONTENIDO
# ============================================================

def clean_markdown(text):
    original = text

    text, blocks = protect_code_blocks(text)
    text = remove_yaml_front_matter(text)
    text = fix_latex_syntax(text)
    text = restore_code_blocks(text, blocks)

    text = remove_all_links(text)
    text = center_images(text)

    return text, text != original


def process_file(file_path, root, dry_run=False):
    file_path = Path(file_path)

    try:
        relative = file_path.relative_to(root)
    except ValueError:
        relative = file_path

    print()
    print("-" * 70)
    print(f"📄 {relative}")

    try:
        original = file_path.read_text(encoding="utf-8-sig")
    except Exception as error:
        print(f"   ❌ Error de lectura: {error}")
        return False

    cleaned, changed = clean_markdown(original)

    if not changed:
        print("   ⚪ Sin cambios requeridos.")
        return False

    print("   🔄 Modificaciones detectadas.")

    if dry_run:
        print("   🔎 DRY-RUN: Archivo no modificado.")
        return True

    try:
        file_path.write_text(cleaned, encoding="utf-8")
        print("   ✅ Archivo actualizado.")
        return True
    except Exception as error:
        print(f"   ❌ Error de escritura: {error}")
        return False


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Limpia Markdown, enlaces, imágenes, y corrige automáticamente sintaxis conflictiva de LaTeX/KaTeX."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Carpeta inicial (por defecto la carpeta actual)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra qué cambiaría sin tocar el disco."
    )

    args = parser.parse_args()
    root = Path(args.root).resolve()

    print()
    print("=" * 70)
    print("      LIMPIADOR DE MARKDOWN Y NORMALIZADOR DE LATEX/KATEX")
    print("=" * 70)
    print(f"\n📁 Escaneando directorio raíz:\n   {root}")

    if not root.exists() or not root.is_dir():
        print("\n❌ Directorio no válido.")
        return

    # 1. Purgar backups .bak previos
    print("\n🧹 Eliminando archivos .bak antiguos...")
    deleted_baks = remove_existing_backups(root, dry_run=args.dry_run)
    if deleted_baks == 0 and not args.dry_run:
        print("   (No se detectaron archivos .bak residuales)")

    # 2. Buscar y procesar archivos markdown
    files_found = list(find_markdown_files(root))
    print(f"\n📚 Archivos Markdown/README encontrados: {len(files_found)}")

    if not files_found:
        print("\n⚠ No se encontraron archivos para procesar.")
        return

    modified_count = 0
    for f in files_found:
        if process_file(f, root, dry_run=args.dry_run):
            modified_count += 1

    # 3. Resumen final
    print()
    print("=" * 70)
    print("                               RESUMEN")
    print("=" * 70)
    print(f"\n📚 Archivos escaneados : {len(files_found)}")
    print(f"✏️️ Archivos modificados : {modified_count}")
    if not args.dry_run:
        print(f"🗑️ Backups eliminados  : {deleted_baks}")
    else:
        print("\n🔎 Modo DRY-RUN completado: ningún archivo fue alterado ni eliminado.")

    print("\n✅ Proceso completado exitosamente.\n")


if __name__ == "__main__":
    main()