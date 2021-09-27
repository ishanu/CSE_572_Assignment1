import pandas as pd

#read the csv file
dfCGM = pd.read_csv("CGMData.csv", low_memory=False, parse_dates=[['Date', 'Time']], keep_date_col=True)
dfInsulin = pd.read_csv("InsulinData.csv", low_memory= False, parse_dates=[['Date', 'Time']], keep_date_col=True)

#finding the auto mode start time
autoModeStartDateTime = dfInsulin[dfInsulin['Alarm'] == 'AUTO MODE ACTIVE PLGM OFF']['Date_Time']

#dropping the missing data for Sensor Glucose
dfCGM.dropna(subset=['Sensor Glucose (mg/dL)'], inplace=True)

dfCGM['Time'] = pd.to_datetime(dfCGM['Time'])

#dividing the data into automode and manualmode
dfCGMManualMode = dfCGM[dfCGM['Date_Time'] < autoModeStartDateTime.iloc[1]]
dfCGMAutoMode = dfCGM[dfCGM['Date_Time'] >= autoModeStartDateTime.iloc[1]]

#grouping the data by date
cgmDataGroupedByDate = dfCGMManualMode.groupby('Date')

overNightHyperglycemiaManual = []
overNightHyperglycemiaCriticalManual = []
overNightInRangeManual = []
overNightInRangeSecondaryManual = []
overNightHypoglycemiaLevel1Manual = []
overNightHypoglycemiaLevel2Manual = []

dayTimeHyperglycemiaManual = []
dayTimeHyperglycemiaCriticalManual = []
dayTimeInRangeManual = []
dayTimeInRangeSecondaryManual = []
dayTimeHypoglycemiaLevel1Manual = []
dayTimeHypoglycemiaLevel2Manual = []

wholeDayHyperglycemiaManual = []
wholeDayHyperglycemiaCriticalManual = []
wholeDayInRangeManual = []
wholeDayInRangeSecondaryManual = []
wholeDayHypoglycemiaLevel1Manual = []
wholeDayHypoglycemiaLevel2Manual = []

manualModeDaysCount = 0

# traversing through the manual mode dates
for element, frame in cgmDataGroupedByDate:

    # calculating only over those days which has minimum 80 percent of 288 data points. ie 231 to 288
    if 231 < len(frame) <= 288:
        manualModeDaysCount += 1
        overNightFrame = frame[
            (frame['Time'] < pd.to_datetime('06:00:00')) & (frame['Time'] >= pd.to_datetime('00:00:00'))]
        dayTimeFrame = frame[
            (frame['Time'] >= pd.to_datetime('06:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]

        wholeDayFrame = frame[
            (frame['Time'] >= pd.to_datetime('00:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]

        # dividing by 288 * 1.0 instead of 288 to convert the number to float
        overNightHyperglycemiaManual.append((len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 180]) / (288 * 1.0)))

        overNightHyperglycemiaCriticalManual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 250]) / (288 * 1.0)))

        overNightInRangeManual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / (288 * 1.0)))

        overNightInRangeSecondaryManual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / (288 * 1.0)))

        overNightHypoglycemiaLevel1Manual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 70]) / (288 * 1.0)))

        overNightHypoglycemiaLevel2Manual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 54]) / (288 * 1.0)))

        dayTimeHyperglycemiaManual.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 180]) / (288 * 1.0)))

        dayTimeHyperglycemiaCriticalManual.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 250]) / (288 * 1.0)))

        dayTimeInRangeManual.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / (288 * 1.0)))

        dayTimeInRangeSecondaryManual.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / (288 * 1.0)))

        dayTimeHypoglycemiaLevel1Manual.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 70]) / (288 * 1.0)))

        dayTimeHypoglycemiaLevel2Manual.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 54]) / (288 * 1.0)))

        wholeDayHyperglycemiaManual.append((len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 180]) / (288 * 1.0)))

        wholeDayHyperglycemiaCriticalManual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 250]) / (288 * 1.0)))

        wholeDayInRangeManual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / (288 * 1.0)))

        wholeDayInRangeSecondaryManual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / (288 * 1.0)))

        wholeDayHypoglycemiaLevel1Manual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 70]) / (288 * 1.0)))

        wholeDayHypoglycemiaLevel2Manual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 54]) / (288 * 1.0)))

# grouping the auto mode data by dates
cgmDataGroupedByDate = dfCGMAutoMode.groupby('Date')

overNightHyperglycemiaAuto = []
overNightHyperglycemiaCriticalAuto = []
overNightInRangeAuto = []
overNightInRangeSecondaryAuto = []
overNightHypoglycemiaLevel1Auto = []
overNightHypoglycemiaLevel2Auto = []

dayTimeHyperglycemiaAuto = []
dayTimeHyperglycemiaCriticalAuto = []
dayTimeInRangeAuto = []
dayTimeInRangeSecondaryAuto = []
dayTimeHypoglycemiaLevel1Auto = []
dayTimeHypoglycemiaLevel2Auto = []

wholeDayHyperglycemiaAuto = []
wholeDayHyperglycemiaCriticalAuto = []
wholeDayInRangeAuto = []
wholeDayInRangeSecondaryAuto = []
wholeDayHypoglycemiaLevel1Auto = []
wholeDayHypoglycemiaLevel2Auto = []

autoModeDaysCount = 0

# traversing through the auto mode dates
for element, frame in cgmDataGroupedByDate:

    # calculating only over those days which has minimum 80 percent of 288 data points. ie 231 to 288
    if 231 < len(frame) <= 288:
        autoModeDaysCount += 1
        overNightFrame = frame[
            (frame['Time'] < pd.to_datetime('06:00:00')) & (frame['Time'] >= pd.to_datetime('00:00:00'))]
        dayTimeFrame = frame[
            (frame['Time'] >= pd.to_datetime('06:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]

        wholeDayFrame = frame[
            (frame['Time'] >= pd.to_datetime('00:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]


        # dividing by 288 * 1.0 instead of 288 to convert the number to float
        overNightHyperglycemiaAuto.append((len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 180]) / (288 * 1.0)))

        overNightHyperglycemiaCriticalAuto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 250]) / (288 * 1.0)))

        overNightInRangeAuto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / (288 * 1.0)))

        overNightInRangeSecondaryAuto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / (288 * 1.0)))

        overNightHypoglycemiaLevel1Auto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 70]) / (288 * 1.0)))

        overNightHypoglycemiaLevel2Auto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 54]) / (288 * 1.0)))

        dayTimeHyperglycemiaAuto.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 180]) / (288 * 1.0)))

        dayTimeHyperglycemiaCriticalAuto.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 250]) / (288 * 1.0)))

        dayTimeInRangeAuto.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / (288 * 1.0)))

        dayTimeInRangeSecondaryAuto.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / (288 * 1.0)))

        dayTimeHypoglycemiaLevel1Auto.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 70]) / (288 * 1.0)))

        dayTimeHypoglycemiaLevel2Auto.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 54]) / (288 * 1.0)))

        wholeDayHyperglycemiaAuto.append((len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 180]) / (288 * 1.0)))

        wholeDayHyperglycemiaCriticalAuto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 250]) / (288 * 1.0)))

        wholeDayInRangeAuto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / (288 * 1.0)))

        wholeDayInRangeSecondaryAuto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / (288 * 1.0)))

        wholeDayHypoglycemiaLevel1Auto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 70]) / (288 * 1.0)))

        wholeDayHypoglycemiaLevel2Auto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 54]) / (288 * 1.0)))


column_names = ['Modes',
                'Over Night Percentage time in hyperglycemia (CGM > 180 mg/dL)',
                'Over Night percentage of time in hyperglycemia critical (CGM > 250 mg/dL)',
                'Over Night percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)',
                'Over Night percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)',
                'Over Night percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)',
                'Over Night percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)',
                'Day Time Percentage time in hyperglycemia (CGM > 180 mg/dL)',
                'Day Time percentage of time in hyperglycemia critical (CGM > 250 mg/dL)',
                'Day Time percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)',
                'Day Time percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)',
                'Day Time percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)',
                'Day Time percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)',
                'Whole Day Percentage time in hyperglycemia (CGM > 180 mg/dL)',
                'Whole Day percentage of time in hyperglycemia critical (CGM > 250 mg/dL)',
                'Whole Day percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)',
                'Whole Day percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)',
                'Whole Day percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)',
                'Whole Day percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)']

resultDf = pd.DataFrame(columns=column_names)
resultDf['Modes'] = ['Manual Mode', 'Auto Mode']

#function to find the final percentage
def output(listValue, daysCount):
    return round((sum(listValue) / daysCount) * 100, 2)

# creating the csv file
resultDf['Over Night Percentage time in hyperglycemia (CGM > 180 mg/dL)'] = [output(overNightHyperglycemiaManual, manualModeDaysCount),
                                                                              output(overNightHyperglycemiaAuto, autoModeDaysCount)]
resultDf['Over Night percentage of time in hyperglycemia critical (CGM > 250 mg/dL)'] = [
    output(overNightHyperglycemiaCriticalManual, manualModeDaysCount), output(overNightHyperglycemiaCriticalAuto, autoModeDaysCount)]
resultDf['Over Night percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)'] = [
    output(overNightInRangeManual, manualModeDaysCount), output(overNightInRangeAuto, autoModeDaysCount)]
resultDf['Over Night percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)'] = [
    output(overNightInRangeSecondaryManual, manualModeDaysCount), output(overNightInRangeSecondaryAuto, autoModeDaysCount)]
resultDf['Over Night percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)'] = [
    output(overNightHypoglycemiaLevel1Manual, manualModeDaysCount), output(overNightHypoglycemiaLevel1Auto, autoModeDaysCount)]
resultDf['Over Night percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)'] = [
    output(overNightHypoglycemiaLevel2Manual, manualModeDaysCount), output(overNightHypoglycemiaLevel2Auto, autoModeDaysCount)]

resultDf['Day Time Percentage time in hyperglycemia (CGM > 180 mg/dL)'] = [output(dayTimeHyperglycemiaManual, manualModeDaysCount),
                                                                            output(dayTimeHyperglycemiaAuto, autoModeDaysCount)]
resultDf['Day Time percentage of time in hyperglycemia critical (CGM > 250 mg/dL)'] = [
    output(dayTimeHyperglycemiaCriticalManual, manualModeDaysCount), output(dayTimeHyperglycemiaCriticalAuto, autoModeDaysCount)]
resultDf['Day Time percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)'] = [
    output(dayTimeInRangeManual, manualModeDaysCount), output(dayTimeInRangeAuto, autoModeDaysCount)]
resultDf['Day Time percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)'] = [
    output(dayTimeInRangeSecondaryManual, manualModeDaysCount), output(dayTimeInRangeSecondaryAuto, autoModeDaysCount)]
resultDf['Day Time percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)'] = [
    output(dayTimeHypoglycemiaLevel1Manual, manualModeDaysCount), output(dayTimeHypoglycemiaLevel1Auto, autoModeDaysCount)]
resultDf['Day Time percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)'] = [
    output(dayTimeHypoglycemiaLevel2Manual, manualModeDaysCount), output(dayTimeHypoglycemiaLevel2Auto, autoModeDaysCount)]

resultDf['Whole Day Percentage time in hyperglycemia (CGM > 180 mg/dL)'] = [output(wholeDayHyperglycemiaManual, manualModeDaysCount),
                                                                             output(wholeDayHyperglycemiaAuto, autoModeDaysCount)]
resultDf['Whole Day percentage of time in hyperglycemia critical (CGM > 250 mg/dL)'] = [
    output(wholeDayHyperglycemiaCriticalManual, manualModeDaysCount), output(wholeDayHyperglycemiaCriticalAuto, autoModeDaysCount)]
resultDf['Whole Day percentage time in range (CGM >= 70 mg/dL and CGM <= 180 mg/dL)'] = [
    output(wholeDayInRangeManual, manualModeDaysCount), output(wholeDayInRangeAuto, autoModeDaysCount)]
resultDf['Whole Day percentage time in range secondary (CGM >= 70 mg/dL and CGM <= 150 mg/dL)'] = [
    output(wholeDayInRangeSecondaryManual, manualModeDaysCount), output(wholeDayInRangeSecondaryAuto, autoModeDaysCount)]
resultDf['Whole Day percentage time in hypoglycemia level 1 (CGM < 70 mg/dL)'] = [
    output(wholeDayHypoglycemiaLevel1Manual, manualModeDaysCount), output(wholeDayHypoglycemiaLevel1Auto, autoModeDaysCount)]
resultDf['Whole Day percentage time in hypoglycemia level 2 (CGM < 54 mg/dL)'] = [
    output(wholeDayHypoglycemiaLevel2Manual, manualModeDaysCount), output(wholeDayHypoglycemiaLevel2Auto, autoModeDaysCount)]
resultDf['dummy'] = [1.1,1.1]

resultDf.set_index('Modes', inplace=True)

resultDf.to_csv('Results.csv', index=False, header=None)
