import streamlit as st
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

st.set_page_config(page_title="🎨 Color Picker", layout="centered")

def extract_colors(image, n_colors=5):
    image = image.resize((150, 150))
    pixels = np.array(image).reshape(-1, 3)
    model = KMeans(n_clusters=n_colors)
    model.fit(pixels)
    centers = model.cluster_centers_.astype(int)
    return ['#%02x%02x%02x' % tuple(c) for c in centers]

def is_dark_color(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    brightness = (r*299 + g*587 + b*114) / 1000
    return brightness < 128

def brightness(hex_color):
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (r*299 + g*587 + b*114) / 1000

def get_alpha_by_brightness(hex_color):
    bright = brightness(hex_color)
    if bright < 80:
        return 0.2
    elif bright < 130:
        return 0.4
    else:
        return 0.85

def get_contrast_color(hex_color):
    return 'rgba(255, 255, 255, 0.5)' if is_dark_color(hex_color) else 'rgba(0, 0, 0, 0.5)'

def color_distance(c1, c2):
    r1, g1, b1 = int(c1[1:3],16), int(c1[3:5],16), int(c1[5:7],16)
    r2, g2, b2 = int(c2[1:3],16), int(c2[3:5],16), int(c2[5:7],16)
    return ((r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2)**0.5

def render_style(bg_colors, is_default=False):
    if is_default:
        bg_css = """
            background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
        """
        text_color = "#000"
        container_bg = "rgba(255, 255, 255, 0.85)"
    else:
        primary = bg_colors[0]
        secondary = bg_colors[1] if len(bg_colors) > 1 else primary

        dist = color_distance(primary, secondary)
        if dist < 40:
            secondary = "#FFFFFF" if not is_dark_color(primary) else "#000000"

        contrast = get_contrast_color(primary)
        bg_css = f"background: linear-gradient(135deg, {primary}, {secondary});"
        text_color = "#fff" if is_dark_color(primary) else "#000"

        r, g, b = tuple(int(primary.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        alpha = get_alpha_by_brightness(primary)
        container_bg = f"rgba({r}, {g}, {b}, {alpha})"

    st.markdown(f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            {bg_css}
            transition: background 0.7s ease;
        }}
        [data-testid="stHeader"] {{
            background-color: transparent;
        }}
        .title {{
            font-size: 36px;
            font-weight: bold;
            color: {text_color};
            text-align: center;
            margin-bottom: 0;
        }}
        .subtext {{
            font-size: 18px;
            color: {text_color};
            text-align: center;
            margin: 4px 0 20px 0;
        }}
        .box {{
            background-color: {container_bg};
            padding: 30px;
            border-radius: 18px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
            margin: 40px auto;
            max-width: 900px;
            min-width: 320px;
        }}
        .color-box {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }}
        .swatch {{
            width: 70px;
            height: 70px;
            border: 2px solid #333;
            border-radius: 12px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            color: #fff;
            font-size: 12px;
            text-shadow: 1px 1px 2px #00000055;
            flex-shrink: 0;
        }}
        .caption-text {{
            font-size: 1.1rem;
            font-weight: 600;
            text-align: center;
            margin: 10px 0 20px 0;
            color: {text_color};
        }}
        .hex-code-title {{
            font-size: 1.25rem;
            font-weight: 700;
            text-align: center;
            margin: 30px 0 10px 0;
            color: {text_color};
        }}
        @media (max-width: 600px) {{
            .caption-text {{ font-size: 1rem; }}
            .hex-code-title {{ font-size: 1.1rem; }}
        }}
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown('<div class="title">🎨 Color Picker</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Upload picture to see 5 dominant colors</div>', unsafe_allow_html=True)

def main():
    render_style([], is_default=True)
    render_header()

    uploaded_file = st.file_uploader("Upload Picture (jpg/png)", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        colors = extract_colors(image)
        render_style(colors, is_default=False)

        with st.spinner("🔍 Analyzing dominant colors..."):
            colors = extract_colors(image)

            st.image(image, use_container_width=True)
            st.markdown('<div class="caption-text">Uploaded Picture</div>', unsafe_allow_html=True)

            swatches_html = ''.join(
                f'<div class="swatch" style="background-color: {hex};">{hex}</div>'
                for hex in colors
            )
            st.markdown(f'<div class="color-box">{swatches_html}</div>', unsafe_allow_html=True)

            st.markdown('<div class="hex-code-title">HEX Color Codes:</div>', unsafe_allow_html=True)
            st.code("\n".join(colors))

if __name__ == "__main__":
    main()
