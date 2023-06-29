# # import sys
# # import os
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # Check if the CSV filename and output folder are provided as command-line arguments
# # if len(sys.argv) < 3:
# #     print("Please provide the CSV filename and the output folder as command-line arguments.")
# #     sys.exit(1)

# # # Get the CSV filename and output folder from the command-line arguments
# # csv_filename = sys.argv[1]
# # output_folder = sys.argv[2]

# # # Read the CSV file
# # data = pd.read_csv(csv_filename)

# # # Create the output folder if it doesn't exist
# # os.makedirs(output_folder, exist_ok=True)

# # # Line Plot
# # plt.plot(data['step'], data['system_total_stopped'])
# # plt.xlabel('Step')
# # plt.ylabel('System Total Stopped')
# # plt.savefig(os.path.join(output_folder, 'line_plot.png'))
# # plt.close()

# # # Bar Plot
# # plt.bar(data['step'], data['system_total_waiting_time'])
# # plt.xlabel('Step')
# # plt.ylabel('System Total Waiting Time')
# # plt.savefig(os.path.join(output_folder, 'bar_plot.png'))
# # plt.close()

# # # Scatter Plot
# # plt.scatter(data['system_mean_speed'], data['system_total_waiting_time'])
# # plt.xlabel('System Mean Speed')
# # plt.ylabel('System Total Waiting Time')
# # plt.savefig(os.path.join(output_folder, 'scatter_plot.png'))
# # plt.close()

# # # Heatmap
# # heatmap_data = data[['system_total_stopped', 'system_total_waiting_time', 'system_mean_waiting_time',
# #                      'system_mean_speed', 't_stopped', 't_accumulated_waiting_time', 't_average_speed',
# #                      'agents_total_stopped', 'agents_total_accumulated_waiting_time']]
# # plt.imshow(heatmap_data.corr(), cmap='coolwarm', interpolation='nearest')
# # plt.xticks(range(len(heatmap_data.columns)), heatmap_data.columns, rotation=45)
# # plt.yticks(range(len(heatmap_data.columns)), heatmap_data.columns)
# # plt.colorbar()
# # plt.savefig(os.path.join(output_folder, 'heatmap.png'))
# # plt.close()

# # # Area Plot
# # plt.fill_between(data['step'], data['system_total_waiting_time'].cumsum(), alpha=0.5)
# # plt.xlabel('Step')
# # plt.ylabel('Cumulative System Total Waiting Time')
# # plt.savefig(os.path.join(output_folder, 'area_plot.png'))
# # plt.close()

# # # Box Plot
# # plt.boxplot(data[['system_total_stopped', 'system_total_waiting_time', 'system_mean_waiting_time']])
# # plt.xlabel('Metrics')
# # plt.ylabel('Values')
# # plt.xticks([1, 2, 3], ['System Total Stopped', 'System Total Waiting Time', 'System Mean Waiting Time'])
# # plt.savefig(os.path.join(output_folder, 'box_plot.png'))
# # plt.close()
# # import sys
# # import os
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # Check if the CSV filename and output folder are provided as command-line arguments
# # if len(sys.argv) < 3:
# #     print("Please provide the CSV filename and the output folder as command-line arguments.")
# #     sys.exit(1)

# # # Get the CSV filename and output folder from the command-line arguments
# # csv_filename = sys.argv[1]
# # output_folder = sys.argv[2]

# # # Read the CSV file
# # data = pd.read_csv(csv_filename)

# # # Create the output folder if it doesn't exist
# # os.makedirs(output_folder, exist_ok=True)

# # # Stacked Area Plot
# # plt.stackplot(data['step'], data['t_stopped'], data['agents_total_stopped'], labels=['t_stopped', 'agents_total_stopped'])
# # plt.xlabel('Step')
# # plt.ylabel('System Total Stopped')
# # plt.legend()
# # plt.savefig(os.path.join(output_folder, 'stacked_area_plot.png'))
# # plt.close()

# # # Line Plot with Multiple Y-Axes
# # fig, ax1 = plt.subplots()
# # ax2 = ax1.twinx()
# # ax1.plot(data['step'], data['system_total_waiting_time'], 'b-', label='System Total Waiting Time')
# # ax2.plot(data['step'], data['system_mean_waiting_time'], 'r-', label='System Mean Waiting Time')
# # ax2.plot(data['step'], data['system_mean_speed'], 'g-', label='System Mean Speed')
# # ax1.set_xlabel('Step')
# # ax1.set_ylabel('System Total Waiting Time', color='b')
# # ax2.set_ylabel('System Mean Waiting Time / System Mean Speed', color='k')
# # ax1.legend(loc='upper left')
# # ax2.legend(loc='upper right')
# # plt.savefig(os.path.join(output_folder, 'multiple_y_axes_plot.png'))
# # plt.close()

# # # Box Plot for Metrics Comparison
# # metrics_to_compare = ['system_total_stopped', 'system_total_waiting_time', 't_accumulated_waiting_time']
# # data_to_compare = data[metrics_to_compare]
# # plt.boxplot(data_to_compare.values, labels=metrics_to_compare)
# # plt.xlabel('Metrics')
# # plt.ylabel('Values')
# # plt.savefig(os.path.join(output_folder, 'box_plot_comparison.png'))
# # plt.close()

# # # Histograms
# # plt.hist(data['system_mean_speed'], bins=10, alpha=0.5, label='System Mean Speed')
# # plt.hist(data['t_average_speed'], bins=10, alpha=0.5, label='t_average_speed')
# # plt.hist(data['system_mean_waiting_time'], bins=10, alpha=0.5, label='System Mean Waiting Time')
# # plt.xlabel('Metric Values')
# # plt.ylabel('Frequency')
# # plt.legend()
# # plt.savefig(os.path.join(output_folder, 'histograms.png'))
# # plt.close()

# # # Scatter Plot Matrix
# # pd.plotting.scatter_matrix(data[['system_total_stopped', 'system_total_waiting_time', 'system_mean_waiting_time',
# #                                  'system_mean_speed', 't_stopped', 't_accumulated_waiting_time',
# #                                  't_average_speed', 'agents_total_stopped', 'agents_total_accumulated_waiting_time']],
# #                            figsize=(10, 10))
# # plt.savefig(os.path.join(output_folder, 'scatter_plot_matrix.png'))
# # plt.close()

# # # Violin Plot
# # plt.violinplot([data['system_total_stopped'], data['agents_total_stopped']], showmedians=True)
# # plt.xticks([1, 2], ['System Total Stopped', 'Agents Total Stopped'])
# # plt.ylabel('Values')
# # plt.savefig(os.path.join(output_folder, 'violin_plot.png'))
# # plt.close()
# # import sys
# # import os
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # Check if the CSV filename and output folder are provided as command-line arguments
# # if len(sys.argv) < 3:
# #     print("Please provide the CSV filename and the output folder as command-line arguments.")
# #     sys.exit(1)

# # # Get the CSV filename and output folder from the command-line arguments
# # csv_filename = sys.argv[1]
# # output_folder = sys.argv[2]

# # # Read the CSV file
# # data = pd.read_csv(csv_filename)

# # # Create the output folder if it doesn't exist
# # os.makedirs(output_folder, exist_ok=True)

# # # Stacked Area Plot
# # plt.stackplot(data['step'], data['t_stopped'], data['agents_total_stopped'], labels=['t_stopped', 'agents_total_stopped'])
# # plt.xlabel('Step')
# # plt.ylabel('System Total Stopped')
# # plt.legend()
# # plt.savefig(os.path.join(output_folder, 'stacked_area_plot.png'), overwrite=True)
# # plt.close()

# # # Line Plot with Multiple Y-Axes
# # fig, ax1 = plt.subplots()
# # ax2 = ax1.twinx()
# # ax1.plot(data['step'], data['system_total_waiting_time'], 'b-', label='System Total Waiting Time')
# # ax2.plot(data['step'], data['system_mean_waiting_time'], 'r-', label='System Mean Waiting Time')
# # ax2.plot(data['step'], data['system_mean_speed'], 'g-', label='System Mean Speed')
# # ax1.set_xlabel('Step')
# # ax1.set_ylabel('System Total Waiting Time', color='b')
# # ax2.set_ylabel('System Mean Waiting Time / System Mean Speed', color='k')
# # ax1.legend(loc='upper left')
# # ax2.legend(loc='upper right')
# # plt.savefig(os.path.join(output_folder, 'multiple_y_axes_plot.png'), overwrite=True)
# # plt.close()

# # # Box Plot for Metrics Comparison
# # metrics_to_compare = ['system_total_stopped', 'system_total_waiting_time', 't_accumulated_waiting_time']
# # data_to_compare = data[metrics_to_compare]
# # plt.boxplot(data_to_compare.values, labels=metrics_to_compare)
# # plt.xlabel('Metrics')
# # plt.ylabel('Values')
# # plt.savefig(os.path.join(output_folder, 'box_plot_comparison.png'), overwrite=True)
# # plt.close()

# # # Histograms
# # plt.hist(data['system_mean_speed'], bins=10, alpha=0.5, label='System Mean Speed')
# # plt.hist(data['t_average_speed'], bins=10, alpha=0.5, label='t_average_speed')
# # plt.hist(data['system_mean_waiting_time'], bins=10, alpha=0.5, label='System Mean Waiting Time')
# # plt.xlabel('Metric Values')
# # plt.ylabel('Frequency')
# # plt.legend()
# # plt.savefig(os.path.join(output_folder, 'histograms.png'), overwrite=True)
# # plt.close()

# # # Scatter Plot Matrix
# # pd.plotting.scatter_matrix(data[['system_total_stopped', 'system_total_waiting_time', 'system_mean_waiting_time',
# #                                  'system_mean_speed', 't_stopped', 't_accumulated_waiting_time',
# #                                  't_average_speed', 'agents_total_stopped', 'agents_total_accumulated_waiting_time']],
# #                            figsize=(10, 10))
# # plt.savefig(os.path.join(output_folder, 'scatter_plot_matrix.png'), overwrite=True)
# # plt.close()

# # # Violin Plot
# # plt.violinplot([data['system_total_stopped'], data['agents_total_stopped'], data['system_total_waiting_time']],
# #                showmedians=True)
# # plt.xticks([1, 2, 3], ['System Total Stopped', 'Agents Total Stopped', 'System Total Waiting Time'])
# # plt.ylabel('Values')
# # plt.savefig(os.path.join(output_folder, 'violin_plot.png'), overwrite=True)
# # plt.close()

# import sys
# import os
# import pandas as pd
# import matplotlib.pyplot as plt

# # Check if the CSV filename and output folder are provided as command-line arguments
# if len(sys.argv) < 3:
#     print("Please provide the CSV filename and the output folder as command-line arguments.")
#     sys.exit(1)

# # Get the CSV filename and output folder from the command-line arguments
# csv_filename = sys.argv[1]
# output_folder = sys.argv[2]

# # Read the CSV file
# data = pd.read_csv(csv_filename)

# # Create the output folder if it doesn't exist
# os.makedirs(output_folder, exist_ok=True)
# # Bar Plot
# plt.bar(data['step'], data['system_total_waiting_time'])
# plt.xlabel('Step')
# plt.ylabel('System Total Waiting Time')
# plt.savefig(os.path.join(output_folder, 'bar_plot.png'))
# plt.close()

# # Stacked Area Plot
# plt.stackplot(data['step'], data['t_stopped'], data['agents_total_stopped'], labels=['t_stopped', 'agents_total_stopped'])
# plt.xlabel('Step')
# plt.ylabel('System Total Stopped')
# plt.legend()

# # Save the figure, removing the existing file if it already exists
# output_path = os.path.join(output_folder, 'stacked_area_plot.png')
# if os.path.exists(output_path):
#     os.remove(output_path)
# plt.savefig(output_path)
# plt.close()

# # Line Plot with Multiple Y-Axes
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
# ax1.plot(data['step'], data['system_total_waiting_time'], 'b-', label='System Total Waiting Time')
# ax2.plot(data['step'], data['system_mean_waiting_time'], 'r-', label='System Mean Waiting Time')
# ax2.plot(data['step'], data['system_mean_speed'], 'g-', label='System Mean Speed')
# ax1.set_xlabel('Step')
# ax1.set_ylabel('System Total Waiting Time', color='b')
# ax2.set_ylabel('System Mean Waiting Time / System Mean Speed', color='k')
# ax1.legend(loc='upper left')
# ax2.legend(loc='upper right')

# # Save the figure, removing the existing file if it already exists
# output_path = os.path.join(output_folder, 'multiple_y_axes_plot.png')
# if os.path.exists(output_path):
#     os.remove(output_path)
# plt.savefig(output_path)
# plt.close()

# # Box Plot for Metrics Comparison
# metrics_to_compare = ['system_total_stopped', 'system_total_waiting_time', 't_accumulated_waiting_time']
# data_to_compare = data[metrics_to_compare]
# plt.boxplot(data_to_compare.values, labels=metrics_to_compare)
# plt.xlabel('Metrics')
# plt.ylabel('Values')

# # Save the figure, removing the existing file if it already exists
# output_path = os.path.join(output_folder, 'box_plot_comparison.png')
# if os.path.exists(output_path):
#     os.remove(output_path)
# plt.savefig(output_path)
# plt.close()

# # Histograms
# plt.hist(data['system_mean_speed'], bins=10, alpha=0.5, label='System Mean Speed')
# plt.hist(data['t_average_speed'], bins=10, alpha=0.5, label='t_average_speed')
# plt.hist(data['system_mean_waiting_time'], bins=10, alpha=0.5, label='System Mean Waiting Time')
# plt.xlabel('Metric Values')
# plt.ylabel('Frequency')
# plt.legend()

# # Violin Plot for system_total_waiting_time
# if data['system_total_waiting_time'].nunique() > 1:
#     plt.figure()
#     plt.violinplot(data['system_total_waiting_time'], showmedians=True)
#     plt.xlabel('Metric')
#     plt.ylabel('System Total Waiting Time')
#     plt.title('Violin Plot: System Total Waiting Time')
#     plt.savefig(os.path.join(output_folder, 'violin_plot_system_total_waiting_time.png'))
#     plt.close()
# else:
#     print("No valid data for system_total_waiting_time. Skipping the violin plot.")

# if os.path.exists(output_path):
#     os.remove(output_path)
# plt.savefig(output_path)
# plt.close()




# Only generating the BAR plots for each csv in a folder
import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Get the path of the current script
current_path = os.path.dirname(os.path.abspath(__file__))

# Get the path to the folder containing the CSV files from command line argument
csv_folder = sys.argv[1]

# Check if the provided path is a directory
if not os.path.isdir(csv_folder):
    print("Error: The provided path is not a directory.")
    sys.exit(1)

# Get a list of CSV files in the folder
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Process each CSV file
for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(os.path.join(csv_folder, csv_file))

    # Get the filename without extension
    filename = os.path.splitext(csv_file)[0]

    # Create the bar plot
    plt.figure()
    plt.bar(df['step'], df['system_total_waiting_time'])
    plt.xlabel('Step')
    plt.ylabel('Total Waiting Time')
    plt.title('Total Waiting Time per Step')

    # Save the bar plot in the same folder as the CSV file
    output_path = os.path.join(csv_folder, f'{filename}.png')
    plt.savefig(output_path)

    # Close the plot
    plt.close()

    print(f"Bar plot saved as: {output_path}")




