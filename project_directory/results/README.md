Location to store results. Output from `src` scripts should be directed to this directory. For each batch of analysis, create a new directory for the date (YYYY-MM-DD_analysis) and within each directory create two folders: `figures` and `output`. `output` should contain any needed output of your scripts that is not a plot, table, visualization, movie, etc.

The `runlog.sh` file is another shell script that when executed should run the appropriate files from the `src` directory and produce the final figures and output.

The final results should be put into a directory labeled `final_results`.
