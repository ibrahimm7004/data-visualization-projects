import os
import matplotlib.pyplot as plt


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


def heatmaps(df, output_dir):
    mz_values = df["Recal m/z"]
    hc_ratios = df["H/C"]
    oc_ratios = df["O/C"]
    nc_ratios = df["N/C"]
    on_ratios = df["O/N"]

    fig, axs = plt.subplots(2, 2, figsize=(20, 10), sharex=True)

    # H/C vs. m/z Heatmap
    hb1 = axs[0, 0].hexbin(mz_values, hc_ratios, gridsize=50,
                           cmap='Blues', edgecolors='none')
    axs[0, 0].set_title('H/C vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[0, 0].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[0, 0].set_ylabel('H/C Ratio', fontsize=10, fontweight='bold')
    cb1 = fig.colorbar(hb1, ax=axs[0, 0])
    cb1.set_label('Density')

    # O/C vs. m/z Heatmap
    hb2 = axs[0, 1].hexbin(mz_values, oc_ratios, gridsize=50,
                           cmap='Greens', edgecolors='none')
    axs[0, 1].set_title('O/C vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[0, 1].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[0, 1].set_ylabel('O/C Ratio', fontsize=10, fontweight='bold')
    cb2 = fig.colorbar(hb2, ax=axs[0, 1])
    cb2.set_label('Density')

    # N/C vs. m/z Heatmap
    hb3 = axs[1, 0].hexbin(mz_values, nc_ratios,
                           gridsize=50, cmap='Reds', edgecolors='none')
    axs[1, 0].set_title('N/C vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[1, 0].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[1, 0].set_ylabel('N/C Ratio', fontsize=10, fontweight='bold')
    cb3 = fig.colorbar(hb3, ax=axs[1, 0])
    cb3.set_label('Density')

    # O/N vs. m/z Heatmap
    hb4 = axs[1, 1].hexbin(mz_values, on_ratios, gridsize=50,
                           cmap='Purples', edgecolors='none')
    axs[1, 1].set_title('O/N vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[1, 1].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[1, 1].set_ylabel('O/N Ratio', fontsize=10, fontweight='bold')
    cb4 = fig.colorbar(hb4, ax=axs[1, 1])
    cb4.set_label('Density')

    plt.tight_layout()

    # Save the figure
    plt.savefig(os.path.join(output_dir, 'heatmaps.png'))
    plt.close()


def sampled_heatmaps(df, output_dir):
    subset_df = df.sample(frac=0.1)  # Sample 10% of the data

    mz_values = subset_df["Recal m/z"]
    hc_ratios = subset_df["H/C"]
    oc_ratios = subset_df["O/C"]
    nc_ratios = subset_df["N/C"]
    on_ratios = subset_df["O/N"]

    fig, axs = plt.subplots(2, 2, figsize=(20, 12), sharex=True)

    # H/C vs. m/z Heatmap
    hb1 = axs[0, 0].hexbin(mz_values, hc_ratios, gridsize=20,
                           cmap='Blues', edgecolors='none')
    axs[0, 0].set_title('H/C vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[0, 0].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[0, 0].set_ylabel('H/C Ratio', fontsize=10, fontweight='bold')
    cb1 = fig.colorbar(hb1, ax=axs[0, 0])
    cb1.set_label('Density')

    # O/C vs. m/z Heatmap
    hb2 = axs[0, 1].hexbin(mz_values, oc_ratios, gridsize=20,
                           cmap='Greens', edgecolors='none')
    axs[0, 1].set_title('O/C vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[0, 1].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[0, 1].set_ylabel('O/C Ratio', fontsize=10, fontweight='bold')
    cb2 = fig.colorbar(hb2, ax=axs[0, 1])
    cb2.set_label('Density')

    # N/C vs. m/z Heatmap
    hb3 = axs[1, 0].hexbin(mz_values, nc_ratios,
                           gridsize=20, cmap='Reds', edgecolors='none')
    axs[1, 0].set_title('N/C vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[1, 0].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[1, 0].set_ylabel('N/C Ratio', fontsize=10, fontweight='bold')
    cb3 = fig.colorbar(hb3, ax=axs[1, 0])
    cb3.set_label('Density')

    # O/N vs. m/z Heatmap
    hb4 = axs[1, 1].hexbin(mz_values, on_ratios, gridsize=20,
                           cmap='Purples', edgecolors='none')
    axs[1, 1].setTitle('O/N vs. m/z Heatmap', fontsize=12, fontweight='bold')
    axs[1, 1].set_xlabel('Recal m/z', fontsize=10, fontweight='bold')
    axs[1, 1].set_ylabel('O/N Ratio', fontsize=10, fontweight='bold')
    cb4 = fig.colorbar(hb4, ax=axs[1, 1])
    cb4.set_label('Density')

    plt.tight_layout()

    # Save the figure
    plt.savefig(os.path.join(output_dir, 'sampled_heatmaps.png'))
    plt.close()
