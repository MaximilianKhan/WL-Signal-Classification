# WL-Signal-Classification

With any machine learning program,you need a lot of data to train a machine learning program/neural network. For the signal analysis application that will automate total file analysis, the program needs to be able to distinguish what waveforms to use in calculations.

I will explain step-by-step on how you can obtain data from any labchart file needed for analysis, put the data in the right area such that a python script can see it, run the program to obtain waveforms for classification, take the waveforms for classification that have been saved in a CSV file to then be classified, run a different python script against those possible waveforms, and recursively and manually classify waveforms in the form of 1’s and 0’s in the CSV file until conditions (around 10,000 waveforms per person) have been reached.


## Download Signal Classification Program

**1.** Download this project as a zip from the top of this page.


## Getting Matlab Data from Labchart

**1.** Open the desired labchart file that you wish to extract waveforms from.

![Image of Labchart](https://s3-us-west-1.amazonaws.com/wl-lab/test-view.png)

**2.** All we need to export are the amplitude and length channels, but we can only export one at a time. We will export the amplitude channel first.

**3.** Go to: *File -> Export*. Since we are exporting the amplitude information, name the file: *“amp-data”*, and export the file as a MATLAB file. (Ignore the image below that specifies the folder under *“WL-Signal-Analysis”*) Export this under the folder *WL-Signal-Classification -> mat-data*. When this is done, click save, and you should then be brought to another screen.

![Image for Matlab1](https://s3-us-west-1.amazonaws.com/wl-lab/amp-data-selection.png)

**4.** On the final screen and under the channels dropdown, only select the first drop down that says *“Channel 1 AMP”*. If the prompt does not automatically set this for you, make sure that you are exporting the entire file. Under the *“Include”* section, have your data exported as 32-bit, including comments and event markers. Finally, under the *“Sampling section”* make sure that you select *“Upsample to same rate”* and leave *“Use simple format”* unselected. When done, click *“Ok”*. It should take more or less a minute for Labchart to export the data. Let it do its thing. It might say *“Unexpected error”* and have the screen flash grey a couple times, but just leave it alone until it is done.

![Image of Amp1](https://s3-us-west-1.amazonaws.com/wl-lab/amp-data-1.png)
![Image of Amp2](https://s3-us-west-1.amazonaws.com/wl-lab/amp-data-2.png)

**5.** Now that the amplitude data has been exported, we need to export the length data. Repeat step 3, but name the MATLAB file as *“length-data”*.

**6.** Repeat step 4, but use channel 3 that says: *“IN 3: Length”*, instead.

![Image of Length3](https://s3-us-west-1.amazonaws.com/wl-lab/length-data-1.png)

**7.** Once Labchart has successfully exported the length data, and you see both your *“amp-data”* and *“length-data”* in the *WL-Signal-Classification -> mat-data folder*, you are clear to move on!


## Install Anaconda

Anaconda is a python package and version manager for whichever system you are using, and is extremely useful. Make sure that it is installed on your system. There are many tutorials online on how to do so. Make sure that the libraries: numpy, scipy, pandas, and matplotlib are installed.
[Link to Anaconda.](https://conda.io/docs/user-guide/install/windows.html)


## Download and Install Visual Studio Code

If you do not have this IDE already, please download and install it.
[Link to Visual Studio Code.](https://code.visualstudio.com/)


## Getting a CSV of Signals to be Classified

Before moving on, I need to explain why you will only be analyzing a slice of the Labchart file. 

Not only are our lab’s Labchart files large and computationally expensive when run through entirely, each person only needs to classify 10,000 possible waveforms. Each file contains many possible waveforms such that when running through the program, it can return around 10,000 of them with-in eight minutes of data. Thus, there is no need to classify the entire file. And, with this being the case, we will run the program to analyze the first eight minutes of the labchart file that you turned into matlab files.

**1.** Double check to make sure that your *“amp-data”* and *“length-data”* are located in *WL-Signal-Classification -> mat-data*.

**2.** Open the WL-Signal-Classification folder in Visual Studio Code.

**3.** Open the integrated terminal in Visual Studio Code - you can find it under the *“View”* tab.

**3.5** (If you are using windows, type *activate base*.)

**4.** Type into the terminal: *python capture-signals.py* . It will take about 12.5 minutes, so find something to do in the meantime.

**5.** After the program has finished running, go back into the folder *WL-Signal-Classification -> captured-signals* to find a csv file containing all of the possible signals that had been processed and found, called: *signals.csv* .


## Classifying Waveforms Using CSV File and VS Code

Now that we have our CSV file containing possible signals broken up into 100 output values that can be easily viewed through some unit-arbitrary time series, we can classify whether waves are or are-not proprioceptive signals. Classify all of the waveforms given to you from running the previous program.

![Photo of Proprioceptive Signal](https://s3-us-west-1.amazonaws.com/wl-lab/manual-data-thumbing-2.PNG)
![Photo of Non-Proprioceptive Signal](https://s3-us-west-1.amazonaws.com/wl-lab/manual-data-thumbing-5.PNG)

Picture 1 *IS* a proprioceptive signal, and picture *IS NOT*. Anything that has a similar shape to picture 1 will be classified as a 1, and anything else like picture 2 will be classified as a 0.

**1.** Open the CSV file to appear in microsoft excel.

**2.** When you open up excel, you will see that each row contains 100 values. Scroll to column CW. This is where you will either be writing a 1 for a signal being a proprioceptive signal, and a 0 for it not, and is after the 100 values.

![Photo of CSV](https://s3-us-west-1.amazonaws.com/wl-lab/csv-data-capture-1.PNG)

**3.** In Visual Studio Code where you imported the project, open the file *single-signal-analyzer.py* .

Look at line 9 where the variable *SIGNAL_IDX* exists. This is what you will use to manually sort through the CSV and observe the wave that is located at whichever row. You will use and set *SIGNAL_IDX* equal to whatever row you want to observe. Say, if you wanted to look at row 1 in the CSV, then I would change *SIGNAL_IDX* to be equal to 1 (i.e.: *SIGNAL_IDX = 1*). If you wanted to look at row 3232, then *SIGNAL_IDX = 3232*.

**4.** Look at CSV as see what row needs to be classified.

**5.** Set *SIGNAL_IDX* equal to that row number.

**6.** In Visual Studio code, open up the the integrated terminal, and run: python *single-signal-analyzer.py* .

**7.** Draw conclusions about the signal.

**8.** CLOSE the graph that appeared.

**9.** Switch over to the CSV, and write 1 if signal, and 0 is not signal.

**10.** (Make sure to save your CSV every so often so that if anything goes wrong, you do not lose the classifications, nor the time that you spent doing this.)

**11.** Repeat steps 4-9 until you complete classifying the CSV file.


## Done

Congratulations on classifying all of those signals! After you are done, please email me through my SJSU email letting me know.