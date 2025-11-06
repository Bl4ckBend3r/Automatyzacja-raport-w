import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def create_plots(df, output_dir):
    os.makedirs(f"{output_dir}/plots", exist_ok=True)
    plt.figure(figsize=(8,5))
    plt.bar(df['region'], df['revenue'], color='royalblue', alpha=0.85)
    plt.title("Przychody wg regionu")
    plt.xlabel("Region")
    plt.ylabel("Przychód (PLN)")
    plot_path = f"{output_dir}/plots/revenue_by_region.png"
    plt.savefig(plot_path, bbox_inches="tight")
    plt.close()
    return plot_path

def generate_pdf(summary, plot_path, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Raport sprzedażowy", ln=True, align="C")
    pdf.image(plot_path, x=20, y=30, w=170)
    pdf.ln(120)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Podsumowanie przychodów:", ln=True)
    for _, row in summary.iterrows():
        pdf.cell(0, 10, f"{row['region']}: {row['revenue']:.2f} PLN", ln=True)
    pdf.output(output_path)
