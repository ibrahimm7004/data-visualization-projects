import os
import pandas as pd
import matplotlib.pyplot as plt
from processing import preprocess_data, further_ratios
from plotting import heatmaps, scatter_plots

input_dir = r'C:\Users\hp\Desktop\bmsis-ysp\Elemental Composition assignments (.csv)'
output_base_dir = r'C:\Users\hp\Desktop\bmsis-ysp\Task6_HC,OC,NC,ON_vs _mz\plots'

# Get a list of all CSV files in the input directory
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]


def scatter_plots(df, output_dir):
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('Elemental Ratios vs. m/z', fontweight='bold', fontsize=16)

    # H/C vs. m/z
    axs[0, 0].scatter(df["Recal m/z"], df["H/C"], color='blue')
    axs[0, 0].set_xlabel("Recal m/z", fontweight='bold', fontsize=14)
    axs[0, 0].set_ylabel("H/C", fontweight='bold', fontsize=14)
    axs[0, 0].set_title("H/C vs m/z", fontweight='bold', fontsize=16)
    num_ticks = 6
    axs[0, 0].xaxis.set_major_locator(plt.MaxNLocator(num_ticks))
    axs[0, 0].yaxis.set_major_locator(plt.MaxNLocator(num_ticks))

    # O/C vs. m/z
    axs[0, 1].scatter(df["Recal m/z"], df["O/C"], color='green')
    axs[0, 1].set_xlabel("Recal m/z", fontweight='bold', fontsize=14)
    axs[0, 1].set_ylabel("O/C", fontweight='bold', fontsize=14)
    axs[0, 1].set_title("O/C vs m/z", fontweight='bold', fontsize=16)
    axs[0, 1].xaxis.set_major_locator(plt.MaxNLocator(num_ticks))
    axs[0, 1].yaxis.set_major_locator(plt.MaxNLocator(num_ticks))

    # N/C vs. m/z
    axs[1, 0].scatter(df["Recal m/z"], df["N/C"], color='red')
    axs[1, 0].set_xlabel("Recal m/z", fontweight='bold', fontsize=14)
    axs[1, 0].set_ylabel("N/C", fontweight='bold', fontsize=14)
    axs[1, 0].set_title("N/C vs m/z", fontweight='bold', fontsize=16)
    axs[1, 0].xaxis.set_major_locator(plt.MaxNLocator(num_ticks))
    axs[1, 0].yaxis.set_major_locator(plt.MaxNLocator(num_ticks))

    # O/N vs. m/z
    axs[1, 1].scatter(df["Recal m/z"], df["O/N"], color='purple')
    axs[1, 1].set_xlabel("Recal m/z", fontweight='bold', fontsize=14)
    axs[1, 1].set_ylabel("O/N", fontweight='bold', fontsize=14)
    axs[1, 1].set_title("O/N vs m/z", fontweight='bold', fontsize=16)
    axs[1, 1].xaxis.set_major_locator(plt.MaxNLocator(num_ticks))
    axs[1, 1].yaxis.set_major_locator(plt.MaxNLocator(num_ticks))

    plt.subplots_adjust(hspace=0.8)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Save the figure
    plt.savefig(os.path.join(output_dir, 'scatter_plots.png'))
    plt.close()


for csv_file in csv_files:
    # Create full file path for the input CSV
    csv_file_path = os.path.join(input_dir, csv_file)

    # Create an output directory based on the CSV file name (without the .csv extension)
    output_dir = os.path.join(output_base_dir, os.path.splitext(csv_file)[0])
    os.makedirs(output_dir, exist_ok=True)

    # Preprocess and calculate further ratios
    df = preprocess_data(csv_file_path)
    df = further_ratios(df)

    # Generate and save plots
    scatter_plots(df, output_dir)
    # heatmaps(df, output_dir)
    # sampled_heatmaps(df, output_dir)

    # Print confirmation message
    print(f"{csv_file} Plots Stored.")
