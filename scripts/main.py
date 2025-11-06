from datetime import datetime
from data_processing import load_data, preprocess, summarize
from report_generator import create_plots, generate_pdf
from email_sender import send_email
from config import *

def main():
    print("Wczytywanie danych...")
    df = load_data(DATA_PATH)
    df = preprocess(df)
    summary = summarize(df)

    print("Tworzenie wykresów i raportu PDF...")
    plot_path = create_plots(summary, OUTPUT_DIR)
    report_path = f"{OUTPUT_DIR}/report_{datetime.now():%Y%m%d}.pdf"
    generate_pdf(summary, plot_path, report_path)

    print("Wysyłanie raportu e-mailem...")
    send_email(report_path)

    print(f"Raport wygenerowany i wysłany: {report_path}")

if __name__ == "__main__":
    main()
