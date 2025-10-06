"""
    Objective
    ----------
    Extracts all body metric values from a screenshot of the ArboLeaf smartphone app result page following a recorded measurement

    # Code Execution Example 
    -------------------------
    python imgDataExtract.py --dir_path "C:/ArboLeaf_Data/Folder_Where_ScreenShots_For_Processing_Will_Be_Placed" --path_output_xls "C:/ArboLeaf_Data/Folder_Where_BodyData_ExcelFile_WillBeSaved"

    # Outputs
    ----------
    Microsoft Excel file used to store data from current and follow-up measurements.  
"""

from __future__ import annotations
import argparse

import os
import os.path
import re
import sys

import copy

import cv2
import img2pdf

import numpy as np
import pandas as pd

import pytesseract
from PIL import Image
from pdf2image import convert_from_path

import seaborn as sns

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import matplotlib.patheffects as path_effects

import mplcursors

import plotly.graph_objects as go

# ---------------------- CLI Flags -----------------------------

def parse_args() -> argparse.Namespace:
    """
    Imports values for necessary start up variables 
    """
    parser = argparse.ArgumentParser(description="Body health statistics extraction from Arboleaf smartphone app screenshots")

    # I/O and general arguments
    parser.add_argument("--dir_path", type=str, required=True, help="Arboleaf scrennshot images collection network location")
    parser.add_argument("--path_output_xls", type=str, required=True, help="Dir location of the excel file where the stats read from images will be saved")

    return parser.parse_args()

# ---------------------- Image Manipulation -----------------------------

def sharpen_and_replace_image(image_path, brightness, contrast):
    """
    Sharpens an image and adjusts brightness and contrast.

    Args:
        image_path (str): Path to the image file
        brightness (float): Value to adjust brightness
        contrast (float): Value to adjust contrast

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        image = cv2.imread(image_path)
        sharpened_image = cv2.addWeighted(
            image, contrast, np.zeros(image.shape, image.dtype), 0, brightness
        )
        cv2.imwrite(image_path, sharpened_image)
        return True
    except Exception as e:
        print(f"Error processing image {image_path}: {str(e)}")
        return False


def jpeg_2_pdf_img2pdf(image_path, pdf_path):
    """
    Converts a jpeg image to PDF using img2pdf.

    Args:
        image_path (str): Path to the JPEG image
        pdf_path (str): Path to save the PDF
    """
    try:
        img = Image.open(image_path)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(img.filename))
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def jpeg_2_pdf_cv(image_path, pdf_path):
    """
    Converts a JPEG image to a PDF using OpenCV and Pillow.

    Args:
        image_path (str): Path to the JPEG image
        pdf_path (str): Path to save the PDF
    """
    try:
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image_rgb)
        pil_image.save(pdf_path)
    except Exception as e:
        print(f"Error converting {image_path} to PDF: {e}")


def extract_text_from_image(image_path):
    """Extracts text from an image using pytesseract."""
    try:
        img = Image.open(image_path)
        return pytesseract.image_to_string(img)
    except Exception as e:
        return f"Error: {e}"


def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF using pytesseract and pdf2image."""
    pages = convert_from_path(pdf_path)
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text

# ---------------------- Image Text Extraction -----------------------------

def remove_first_two_lines(text):
    """Removes the first two lines from the given text."""
    lines = text.splitlines(True)
    if len(lines) > 2:
        return ''.join(lines[2:])
    elif len(lines) > 0:
        return ''
    return text


def remove_lines_without_numbers(str_content):
    """Removes lines without numeric characters from the text."""
    return_str_content = ''
    lines = str_content.splitlines()
    for line in lines:
        if re.search(r'\d', line):
            return_str_content += line + "\r\n"
    return return_str_content


def replace_except_numbers_dots(text):
    """Replaces all characters except numbers and dots with spaces."""
    return re.sub(r"[^0-9\.]", " ", text)


def replace_multiple_spaces(text):
    """Replaces multiple spaces with a single space."""
    return re.sub(r"\s+", " ", text)


def replace_bad_characters(text):
    """Replaces bad characters with spaces.

    Args:
        text: The input string.

    Returns:
        The string without the bad chars, or the original string if no bad chars waere found.
    """

    bad_chars = ['1b']
    for c in bad_chars:
        text = re.sub(c, " ", text)
    return text

def remove_trailing_period(input_string):
    """
    Removes the trailing period from a string, if present.

    Args:
        input_string: The string to process.

    Returns:
        The string with the trailing period removed, or the original string if no period was found.
    """
    if input_string and input_string[-1] == '.':
        return input_string[:-1]
    return input_string

# ----------------- Looping through Images Ready for Processing & Text Extraction -----------------

def process_jpg_files(args):
    """
    Iterates through the ArboLeaf daily screenshot jpg files found at dir_path, 
    extracts the body stats from the image and updates the MS Excel file where 
    all results are saved.

    Args:
        dir_path (str): The directory path to browse

    Returns: 
        Nothing, but after the function executes the MS Excel file should  
        include all body statistics. 
    """

    try:
        for jpeg_file in os.scandir(args.dir_path):
            if jpeg_file.is_file():
                # Splits the filename into root and extension
                root, ext = os.path.splitext(jpeg_file.name)

                # Compares the extracted extension with the target extension (case-insensitive)
                if ext.lower() == '.jpg' or  ext.lower() == '.jpeg':

                    full_pdf_file_path = args.dir_path + '/' + jpeg_file.name.replace('jpg', 'pdf').replace('jpeg', 'pdf')
                    reading_date = jpeg_file.name.replace('_', '/').replace('.jpg', '').replace('.jpeg', '')

                    # Process image
                    sharpen_and_replace_image(jpeg_file, 1, 0.5)
                    jpeg_2_pdf_img2pdf(jpeg_file, full_pdf_file_path)

                    # Extract and clean text
                    extracted_text = extract_text_from_pdf(full_pdf_file_path)
                    extracted_text = remove_first_two_lines(extracted_text)
                    print("pre-processed: ", extracted_text)

                    extracted_text = remove_lines_without_numbers(extracted_text)
                    extracted_text = replace_bad_characters(extracted_text)
                    extracted_text = replace_except_numbers_dots(extracted_text)
                    extracted_text = replace_multiple_spaces(extracted_text)
                    extracted_text = extracted_text.split()
                    extracted_text = [remove_trailing_period(item) for item in extracted_text]
                    print("after-processing: ", extracted_text)

                    # Initialize dictionary with metrics
                    Msmnt_Vars = {
                        'Reading_Date': reading_date
                    }

                    if extracted_text[0][-1] == '.':
                        extracted_text[0] = extracted_text[0][:-1]

                    Msmnt_Vars['Weight'] = float("{:.3f}".format(float(extracted_text[0])))
                    Msmnt_Vars['Body Fat'] = float("{:.3f}".format(float(extracted_text[1]) / 100.0))
                    Msmnt_Vars['BMI'] = extracted_text[2]
                    Msmnt_Vars['Skeletal Muscle'] = float("{:.3f}".format(float(extracted_text[3]) / 100.0))
                    Msmnt_Vars['Muscle Mass'] = float("{:.1f}".format(float(extracted_text[4])))
                    Msmnt_Vars['Muscle Storage Ability Level'] = float(extracted_text[5])
                    Msmnt_Vars['Protein'] = float("{:.3f}".format(float(extracted_text[6]) / 100.0))
                    Msmnt_Vars['BMR'] = float(extracted_text[7])
                    Msmnt_Vars['Fat-Free Body Weight'] = float(extracted_text[8])
                    Msmnt_Vars['Subcutaneous Fat'] = float("{:.3f}".format(float(extracted_text[9]) / 100.0))
                    Msmnt_Vars['Visceral Fat'] = float(extracted_text[10])
                    Msmnt_Vars['Body Water'] = float("{:.3f}".format(float(extracted_text[11]) / 100.0))
                    Msmnt_Vars['Bone Mass'] = float(extracted_text[12])

                    print(Msmnt_Vars)

                    # Export to Excel
                    df = pd.DataFrame(data=Msmnt_Vars, index=[0])

                    if not os.path.exists(args.path_output_xls):
                        df.to_excel(args.path_output_xls, index=False)
                    else:
                        existing_df = pd.read_excel(args.path_output_xls)

                        # if the new record has the same date with an existing 
                        # then it drops the latter and keeps the former
                        existing_df = existing_df.drop(existing_df[existing_df['Reading_Date'] == reading_date].index)

                        new_df = pd.DataFrame(data=Msmnt_Vars, index=[0])
                        
                        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
                        combined_df.to_excel(args.path_output_xls, index=False)
    except FileNotFoundError:
        print(f"Error: dir not found at '{args.dir_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# ------------------------------- MAIN ----------------------------------------------------------

def main():
    """
    Main function  
    """

    args = parse_args()

    # checks whether the dir with the source jpeg file(s) exist 
    if not os.path.exists(args.dir_path):
        print(" ****************** cannot find jpeg file or jpeg file has the wrong name **********************")
        sys.exit

    process_jpg_files (args)

if __name__ == "__main__":
    main()

#  ------------------------------ PLOTTING ------------------------------------------------------

args=parse_args()

# Inter-Variable Correlation Matrix
df = pd.read_excel(args.path_output_xls)
df_noDate = df.drop(columns=['Reading_Date'])
corr_matrix = df_noDate.corr()

#  ------------------------------ 1st PLOT ------------------------------------------------------

# Generates a correlation matrix visualizing the relationships between all collected body statistic pairs
# from ArboLeaf app screenshots.

plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix - All Variables')
plt.xticks(rotation=45, ha='right')
plt.show()

#  ------------------------------ 2nd PLOT ------------------------------------------------------

# Generates a correlation matrix visualization of the relationships between all collected body statistic 
# pairs from ArboLeaf app screenshots, eliminating the main diagonal and filtering for those 
# abs(correlations) above a given threshold. 

# sets a correlation threshold (e.g., 0.8)
corr_threshold = 0.8

# creates a deep copy of the original corr matrix df
corr_matrix_copy = copy.deepcopy(corr_matrix)

# create a boolean mask for the upper triangular part of the corr matrix df
# (while keeping the diagonal), using k=1 that means all elements above the
# diagonal are included.
mask = np.triu(np.ones_like(corr_matrix_copy, dtype=bool), k=1)

# apply the mask to corr matrix df to set the upper triang part of it to NaN
filtered_corr = corr_matrix_copy.where(~mask)

# removes all cells with abs(values) lower than the threshold
filtered_corr = filtered_corr.mask(abs(filtered_corr) < corr_threshold)

# removes the main diagonal
np.fill_diagonal(filtered_corr.values, np.nan)

# plots the filtered correlations using Seaborn
plt.figure(figsize=(10, 10))  # Adjust figure size as needed
sns.heatmap(filtered_corr,
    annot=True,             # display the corr values on the heatmap
    cmap="coolwarm",        # color map for the heatmap
    fmt=".2f",              # format annotations to 2 decimal points
    linewidths=0.5,         # add lines between cells
    cbar_kws={'label': 'Correlation Coefficient'})

plt.title(f"Correlation Matrix - Variables with abs(corr coef) >= {corr_threshold}")
plt.xticks(rotation=20, ha='right')
plt.show()

#  ------------------------------ 3rd PLOT ------------------------------------------------------

# Displays the correlation matrix values numerically in the upper triangular portion, and their heatmap 
# visualization where variable-sized squares with color gradients indicate the strength of the correlation coefficients 

# Prepare the figure
fig, ax = plt.subplots(figsize=(10, 8))

# Normalize correlation values for the colormap
norm = Normalize(vmin=-1, vmax=1)
cmap = plt.cm.coolwarm

# Keep references for interactive cursor
annotations = []

# Draw lower triangle rounded squares with shadow
for i in range(len(corr_matrix)):
    for j in range(i):
        corr_value = corr_matrix.iloc[i, j]
        if pd.notnull(corr_value):
            size = abs(corr_value)
            color = cmap(norm(corr_value))
            # Create a rounded box (FancyBboxPatch)
            box = FancyBboxPatch(
                (j - size/2, i - size/2),
                size, size,
                boxstyle="round,pad=0.02,rounding_size=0.1",
                linewidth=0.5, edgecolor='grey', facecolor=color
            )
            # Add shadow path effect
            box.set_path_effects([path_effects.SimpleLineShadow(offset=(1, -1), alpha=0.3),
                                  path_effects.Normal()])
            ax.add_patch(box)

            # Store for cursor interactivity
            annotations.append((box, corr_value))

# Draw correlation numbers in the upper triangle, colored by correlation
texts = []
for i in range(len(corr_matrix)):
    for j in range(i+1, len(corr_matrix)):
        corr_value = corr_matrix.iloc[i, j]
        if pd.notnull(corr_value):
            color = cmap(norm(corr_value))
            txt = ax.text(j, i, f"{corr_value:.2f}", ha='center', va='center',
                          fontsize=9, color=color)
            texts.append((txt, corr_value))

# Set ticks
ax.set_xticks(np.arange(len(corr_matrix)))
ax.set_yticks(np.arange(len(corr_matrix)))
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
ax.set_xticklabels(corr_matrix.columns, rotation=90)
ax.set_yticklabels(corr_matrix.columns)

# Set limits and aspect ratio
ax.set_xlim(-0.5, len(corr_matrix)-0.5)
ax.set_ylim(len(corr_matrix)-0.5, -0.5)
ax.set_aspect('equal')

# Add subtle dashed light silver gridlines
ax.grid(which='both', color='lightgrey', linestyle='--', linewidth=0.7, alpha=0.5)

# Add colorbar
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Correlation')

# Add interactive hover tooltips
cursor = mplcursors.cursor(highlight=True)

# Add tooltips for boxes and texts
@cursor.connect("add")
def on_add(sel):
    for artist, corr_value in annotations + texts:
        if sel.artist == artist:
            sel.annotation.set_text(f"Corr: {corr_value:.2f}")
            sel.annotation.get_bbox_patch().set(fc="white", alpha=0.8)
            break

plt.tight_layout()
plt.title("Correlation Matrix \n Split numerical and heatmap", loc='left', x=-0.40, y=1.25)
plt.show()

#  ------------------------------ 4th PLOT ------------------------------------------------------

# Displays the correlation matrix in an advanced interactive HTML format with beautiful SVG-rounded 
# squares and cluster-colored borders with interactive hover popups showing exact correlations.

# ───────────────────────────────────────────────────────────────────────────────────────────────────
# Mini visualization options for correlation strength that DO NOT differentiate between + and - coeffs
# mini_bar, mini_dots, strength_text, block_gradient, stars
# ───────────────────────────────────────────────────────────────────────────────────────────────────

def mini_bar(v):
    blocks = ["▁","▂","▃","▄","▅","▆","▇","█"]
    idx = min(int(abs(v) * (len(blocks)-1)), len(blocks)-1)
    return blocks[idx] * 5

def mini_dots(v):
    count = max(1, int(abs(v)*8))
    return "●" * count

def strength_text(v):
    pct = abs(v) * 100
    if pct >= 75:
        return "Strength: High"
    elif pct >= 50:
        return "Strength: Medium"
    else:
        return "Strength: Low"

def block_gradient(v):
    blocks = ["░","▒","▓","█"]
    idx = min(int(abs(v) * len(blocks)), len(blocks)-1)
    return blocks[idx] * 5

def stars(v):
    count = max(1, int(abs(v)*5))
    return "★" * count

# ────────────────────────────────────────────────────────────────────────────────────────────
# Mini visualization options for correlation strength that DO differentiate between + and - coeffs
# mini_arrows, mini_plusminus, signed_stars, signed_blocks
# ────────────────────────────────────────────────────────────────────────────────────────────

def mini_arrows(v):
    """
    Shows right arrows for positive, left arrows for negative.
    Length reflects magnitude.
    """
    count = max(1, int(abs(v)*8))
    return "→"*count if v >= 0 else "←"*count

def mini_plusminus(v):
    """
    Shows repeated '+' for positive and '-' for negative.
    """
    count = max(1, int(abs(v)*8))
    return "+"*count if v >= 0 else "-"*count

def signed_stars(v):
    """
    Uses stars for positive and diamonds for negative.
    """
    count = max(1, int(abs(v)*5))
    return "★"*count if v >= 0 else "◆"*count

def signed_blocks(v):
    """
    Uses filled blocks for positive vs hollow/alternate for negative.
    """
    blocks_pos = ["▁","▂","▃","▄","▅","▆","▇","█"]
    blocks_neg = ["░","▒","▓","█","▓","▒","░"," "]
    idx = min(int(abs(v)*(len(blocks_pos)-1)), len(blocks_pos)-1)
    return blocks_pos[idx]*5 if v >= 0 else blocks_neg[idx]*5

# number of discrete colors to sample from the colormap
cmap_numb_discr_colors = 65355 + 1      # leave the + 1 to ensure color normalized values range from 0 to 1

def mpl_to_plotly(cmap_name, n=cmap_numb_discr_colors):
    """
    Creates a Plotly colorscale that tries to match a Matplotlib's colormap
    
    Parameters:
    - n: number of discrete colors to sample from the colormap (default:cmap_numb_discr_colors)
    
    Returns:
    - A list of lists representing the Plotly colorscale
    """

    # Gets the colormap from matplotlib
    cmap = plt.get_cmap(cmap_name)

    scale = []

    # Converts to Plotly format: list of [position, rgb] pairs
    for i in range(n):
        v = i / (n - 1)
        rgb = cmap(v)[:3]
        rgb_str = f"rgb({int(rgb[0]*255)}, {int(rgb[1]*255)}, {int(rgb[2]*255)})"
        scale.append([v, rgb_str])

    return scale

def get_rgba_from_custom_cmap(v, colorscale, alpha=1.0):
    """
    Given a value in [-1,1], normalize to [0,1] and return an rgba string
    based on the custom Plotly colorscale (format must be [[float, 'rgb(...)'],...]).
    """
    # Normalize to 0-1
    norm_v = (v + 1) / 2
    # Ensure it's between 0 and 1
    norm_v = max(0, min(norm_v, 1))

    # Find nearest stop in colorscale
    distances = [abs(norm_v - stop[0]) for stop in colorscale]
    idx = distances.index(min(distances))

    # Extract RGB string
    rgb_str = colorscale[idx][1]  # e.g. "rgb(230,97,1)"
    
    # Parse to retrieve integer components
    rgb_parts = rgb_str.strip("rgb()").split(",")
    r, g, b = [int(x) for x in rgb_parts]

    # Build rgba string 
    return f"rgba({r},{g},{b},{alpha})"

# Builds the custom color Plotly scale that tries to match Matplotlib's colomap
custom_colorscale = mpl_to_plotly('coolwarm', cmap_numb_discr_colors)

clusters = {'Weight':'Body Metrics','BMI':'Body Metrics','Body Fat':'Body Composition',
 'Skeletal Muscle':'Body Composition','Muscle Mass':'Body Composition',
 'Muscle Storage Ability Level':'Metabolic','Protein':'Metabolic','BMR':'Metabolic',
 'Fat-Free Body Weight':'Body Composition','Subcutaneous Fat':'Body Composition',
 'Visceral Fat':'Body Composition','Body Water':'Body Composition','Bone Mass':'Body Composition'}

colors = {'Body Metrics':'blue','Body Composition':'brown','Metabolic':'green'}

fig = go.Figure()

# Creates scatter squares grouped by cluster
for cluster_name, border_color in colors.items():
    x_vals = []; y_vals = []; sizes = []; fill_colors = []; hover_texts = []
    
    for i in range(len(corr_matrix)):
        for j in range(len(corr_matrix)):
            if i == j:
                # faint diagonal
                x_vals.append(corr_matrix.columns[j])
                y_vals.append(corr_matrix.columns[i])
                sizes.append(10)  # fixed small size
                fill_colors.append("rgba(200,200,200,1.0)")  # faint light gray
                hover_texts.append(f"<b>Corr:</b> 1.00<br><i>Diagonal</i>")
                continue
            
            v = corr_matrix.iloc[i, j]
            
            var_cluster = clusters.get(corr_matrix.columns[j], 'Other')
            
            if pd.notnull(v) and var_cluster == cluster_name:
                x_vals.append(corr_matrix.columns[j])
                y_vals.append(corr_matrix.columns[i])
                sizes.append(abs(v)*40)
                fill_colors.append(get_rgba_from_custom_cmap(v, custom_colorscale, 1.0))
                hover_texts.append(
                    f"<b style='color:#222'>Corr:</b> <span style='color:#c084fc'>{v:.2f}</span><br>"
                    f"<span style='color:#d8b4fe'><i>Cluster: {cluster_name}</i></span><br>"
                    f"<span style='font-family:monospace;color:#c084fc'>{mini_plusminus(v)}</span>"
                )
    fig.add_trace(go.Scatter(
        x=x_vals, y=y_vals, mode='markers',
        marker=dict(symbol='square', size=sizes, color=fill_colors, 
                    line=dict(color=border_color, width=2)),
        text=hover_texts, hoverinfo='text',
        name=cluster_name,
        legendgroup=cluster_name,
        # legendgrouptitle_text="Clusters",
        showlegend=True
    ))

# Configure layout
col_order = list(corr_matrix.columns)

fig.update_layout(
    xaxis=dict(categoryorder="array", categoryarray=col_order, side='top'),
    yaxis=dict(categoryorder="array", categoryarray=col_order, autorange='reversed'),
    title=dict(text='Interactive Correlation Matrix', y=0.97),
    width=1200, height=1000,
    plot_bgcolor='white',
    legend=dict(title='<b>Clusters</b>', x=1.05, y=0.9,
                bgcolor='rgba(255,255,255,0.6)', bordercolor='grey', borderwidth=1),
    hoverlabel=dict(
        bgcolor="#fef9c7",  # pale lemon yellow
        font_size=12,
        font_family="Arial"
    )
)

# Creates scatter for colorbar legend based on custom colorscale
z_vals = np.linspace(-1, 1, cmap_numb_discr_colors)

# Builds a color legend based on the customized Plotly colorscale 
# that tries to match matplotlib's selected color pallette
fig.add_trace(go.Scatter(
    x=[None]*len(z_vals),
    y=[None]*len(z_vals),
    mode='markers',
    marker=dict(
        size=0.001,
        color=z_vals,
        colorscale=custom_colorscale,
        cmin=-1, cmax=1,
        colorbar=dict(
            title="Correlation<br>Strength",
            x=1.12,      # <<<-- shifts colorbar to the RHS of the correlation matrix
            len=0.7,
            y=0.4
        )
    ),
    showlegend=False
))

fig.write_html('C:/ArboLeaf_Data/correlation_svg_curved_clusters.html')