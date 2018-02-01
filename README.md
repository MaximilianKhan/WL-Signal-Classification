# WL-Signal-Classification

With any machine learning program,you need a lot of data to train a machine learning program/neural network. For the signal analysis application that will automate total file analysis, the program needs to be able to distinguish what wave forms to use in calculations.

I will explain step-by-step on how you can obtain data from any labchart file needed for analysis, put the data in the right area such that a python script can see it, run the program to obtain waveforms for classification, take the waveforms for classification that have been saved in a CSV file to then be classified, run a different python script against those possible wave-forms, and recursively and manually classify waveforms in the form of 1’s and 0’s in the CSV file until conditions (around 10,000 waveforms per person) have been reached.


## Download Signal Classification Program

**1.** Download the project as a zip from this page.


## Getting Matlab Data from Labchart

**1.** Open your desired labchart file that you with to extract waveforms from.

(insert photo)

**2.** All we need to export are the amplitude and length channels, but we can only do one at a time. We will do the amplitude channel first.

**3.** Go to: File -> Export. Since we are exporting the amplitude information, name the file: “amp-data”, and export the file as a MATLAB file. (Ignore the image where is says “WL-Signal-Analysis”) Export this under the folder “WL-Signal-Classification” -> “mat-data”. When this is done, click save, and you should then be brought to another screen.

(insert photo)

**4.** Before Labchart completes exporting the data, you have to specify some parameters. Under the channels dropdown, only select the first drop down that says “Channel 1 AMP”. If the prompt doesn’t automatically set this for you, make sure that you are exporting the entire file. Under the “Include” section, have your data exported as 32-bit, including comments and event markers. Finally, used the “Samping section,” make sure that you select “Upsample to same rate” and leave “Use simple format” unselected. When done, click “Ok”. It should take more or less a minute for Labchart to export the data. Let it do its thing. It might say “Unexpected error” and have the screen flash grey a couple times, but just leave it alone until it is done.

(insert photo)
(insert photo)

**5.** Now that the amplitude data has been exported, we need to export the length data. Repeat step 3, but name the MATLAB file as “length-data”.

**6.** Repeat step 4, but use channel 3 that says: “IN 3: Length”, instead.

(insert photo)

**7.** Once Labchart has successfully exported the length data, and you see both your “amp-data” and “length-data” in the WL-Signal-Classification -> mat-data folder, you are clear to move on!


## Install Anaconda

Anaconda is a python package and version manager for whichever system you are using, and is extremely useful. Make sure that it is installed on your system, and there are many tutorials online on how to do so.


## Getting a CSV of Signals to be Classified

Before moving on, I need to explain why you will only be analyzing a slice of the Labchart file. 

Not only are our lab’s Labchart files large and computationally expensive when run through entirely, each person only needs to classify 10,000 possible wave forms. Each file contains many possible waveforms such that when running through the program, it can return around 10,000 of them with-in a eight minutes of data. Thus, there is no need to classify the entire file. And, with this being the case, we will run the program to analyze the first eight minutes of the labchart file that you turned into matlab files.

**1.** Double check to make sure that your “amp-data” and “length-data” is located in WL-Signal-Classification -> mat-data.

**2.** Open the WL-Signal-Classification folder in Visual Studio Code.

**3.** Open the integrated terminal in Visual Studio Code - you can find it under the “view” tab.

**4.** Type into the terminal: python capture-signals.py It will take about 12.5 minutes, so find something to do in the meantime.

**5.** After the program has finished running, go back into the folder WL-Signal-Classification -> captured-signals to find a csv file containing all of the possible signals that had been processed and found, called: signals.csv .


## Classifying Waveforms Using CSV File and VS Code

Now that we have our CSV file containing possible signals broken up into 100 output values that can be easily viewed through some unit-arbitrary time series, we can classify whether waves are or are-not proprioceptive signals. Classify all of the waveforms given to you from running the previous program.

Now observe these pictures:

(insert photo)
(insert photo)

Picture 1 IS a proprioceptive signal, and picture IS NOT. Anything that has a similar shape to picture 1 will be classified as a 1, and anything else like picture 2 will be classified as a 0.

**1.** Open the CSV file to appear in microsoft excel.

**2.** When you open up excel, you will see that each row contains 100 values. Scroll to column CW. This is where you will either be writing a 1 for a signal being a proprioceptive signal, and a 0 for it not, and is after the 100 values.

(insert photo)

**3.** In Visual Studio Code where you imported the project, open the file single-signal-analyzer.py .

Look at line 9 where the variable SIGNAL_IDX exists. This is what you will use to manually sort through the CSV and observe the wave that is located at whichever row. You will use and set SIGNAL_IDX equal to whatever row you want to observe. Say, if you wanted to look at row 1 in the CSV, then I would change SIGNAL_IDX to be equal to 1 (i.e.: SIGNAL_IDX = 1). If you wanted to look at row 3232, then SIGNAL_IDX = 3232.

**4.** Look at CSV as see what row needs to be classified.

**5.** Set SIGNAL_IDX equal to that row number.

**6.** In Visual Studio code, open up the the integrated terminal, and run: python single-signal-analyzer.py .

**7.** Draw conclusions about the signal.

**8.** CLOSE the graph that appeared.

**9.** Switch over to the CSV, and write 1 if signal, and 0 is not signal.

**10.** (Make sure to save your CSV every so often so that if anything goes wrong, you do not lose the classifications, nor the time that you spent doing this.)

**11.** Repeat steps  unt4-9 until you complete classifying the CSV file.


## Done

Congratulations on classifying all of those signals! After you are done, please email me through my SJSU email letting me know.