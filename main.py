import pandas as pd

dfCGM = pd.read_csv("CGMData.csv", parse_dates=[['Date', 'Time']], keep_date_col=True)
dfInsulin = pd.read_csv("InsulinData.csv", parse_dates=[['Date', 'Time']], keep_date_col=True)

autoModeStartDateTime = dfInsulin[dfInsulin['Alarm'] == 'AUTO MODE ACTIVE PLGM OFF']['Date_Time']

dfCGM.dropna(subset=['Sensor Glucose (mg/dL)'], inplace=True)
dfCGM['Time'] = pd.to_datetime(dfCGM['Time'])

dfCGMManualMode = dfCGM[dfCGM['Date_Time'] < autoModeStartDateTime.iloc[1]]
dfCGMAutoMode = dfCGM[dfCGM['Date_Time'] >= autoModeStartDateTime.iloc[1]]

cgmDataGroupedByDate = dfCGMManualMode.groupby('Date')
# print(dfCGMManualMode.groupby("Date")["Time"].count())

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

for element, frame in cgmDataGroupedByDate:

    if 231 < len(frame) <= 288:
        manualModeDaysCount += 1
        # print(len((frame)))
        overNightFrame = frame[
            (frame['Time'] < pd.to_datetime('06:00:00')) & (frame['Time'] >= pd.to_datetime('00:00:00'))]
        dayTimeFrame = frame[
            (frame['Time'] >= pd.to_datetime('06:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]

        wholeDayFrame = frame[
            (frame['Time'] >= pd.to_datetime('00:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]

        overNightHyperglycemiaManual.append((len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 180]) / 288))

        overNightHyperglycemiaCriticalManual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 250]) / 288))

        overNightInRangeManual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / 288))

        overNightInRangeSecondaryManual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / 288))

        overNightHypoglycemiaLevel1Manual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 70]) / 288))

        overNightHypoglycemiaLevel2Manual.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 54]) / 288))

        dayTimeHyperglycemiaManual.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 180]) / 288))

        dayTimeHyperglycemiaCriticalManual.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 250]) / 288))

        dayTimeInRangeManual.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / 288))

        dayTimeInRangeSecondaryManual.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / 288))

        dayTimeHypoglycemiaLevel1Manual.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 70]) / 288))

        dayTimeHypoglycemiaLevel2Manual.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 54]) / 288))

        wholeDayHyperglycemiaManual.append((len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 180]) / 288))

        wholeDayHyperglycemiaCriticalManual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 250]) / 288))

        wholeDayInRangeManual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / 288))

        wholeDayInRangeSecondaryManual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / 288))

        wholeDayHypoglycemiaLevel1Manual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 70]) / 288))

        wholeDayHypoglycemiaLevel2Manual.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 54]) / 288))

cgmDataGroupedByDate = dfCGMAutoMode.groupby('Date')

'''
print('overnight manual')
print((sum(overNightHyperglycemiaManual) / count) * 100)

print((sum(overNightHyperglycemiaCriticalManual) / count) * 100)

print((sum(overNightInRangeManual) / count) * 100)

print((sum(overNightInRangeSecondaryManual) / count) * 100)

print((sum(overNightHypoglycemiaLevel1Manual) / count) * 100)

print((sum(overNightHypoglycemiaLevel2Manual) / count) * 100)

print('dayTime manual')
print((sum(dayTimeHyperglycemiaManual) / count) * 100)

print((sum(dayTimeHyperglycemiaCriticalManual) / count) * 100)

print((sum(dayTimeInRangeManual) / count) * 100)

print((sum(dayTimeInRangeSecondaryManual) / count) * 100)

print((sum(dayTimeHypoglycemiaLevel1Manual) / count) * 100)

print((sum(dayTimeHypoglycemiaLevel2Manual) / count) * 100)

print('whole day')
print((sum(wholeDayHyperglycemiaManual) / count) * 100)

print((sum(wholeDayHyperglycemiaCriticalManual) / count) * 100)

print((sum(wholeDayInRangeManual) / count) * 100)

print((sum(wholeDayInRangeSecondaryManual) / count) * 100)

print((sum(wholeDayHypoglycemiaLevel1Manual) / count) * 100)

print((sum(wholeDayHypoglycemiaLevel2Manual) / count) * 100)'''

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

# idhar
'''res = []
for key, subset in cgmDataGroupedByDate:
    total_count = len(subset)
    res.append(((key), total_count))
res_automode = pd.DataFrame(res, columns=['Date', 'DataCounts'])
res_automode = pd.merge(dfCGMAutoMode,
                       res_automode[['Date']][(res_automode['DataCounts'] > 231) & (res_automode['DataCounts'] <= 288)],
                       on='Date')
res_automode['Date'] = pd.to_datetime(res_automode['Date'], format='%m/%d/%Y')
res_automode = res_automode[(res_automode['DataCounts'] > 231) & (res_automode['DataCounts'] <= 288)]
resGroupedByDate = res_automode.groupby('Date')'''
'''res = []
count = 0
for key, frame in cgmDataGroupedByDate:
    if 231 < len(frame) <= 288:
        count = count + len(frame)

        res.append(((key), len(frame)))'''

autoModeDaysCount = 0
for element, frame in cgmDataGroupedByDate:

    if 231 < len(frame) <= 288:
        autoModeDaysCount += 1
        # print(len((frame)))
        overNightFrame = frame[
            (frame['Time'] < pd.to_datetime('06:00:00')) & (frame['Time'] >= pd.to_datetime('00:00:00'))]
        dayTimeFrame = frame[
            (frame['Time'] >= pd.to_datetime('06:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]

        wholeDayFrame = frame[
            (frame['Time'] >= pd.to_datetime('00:00:00')) & (frame['Time'] <= pd.to_datetime('23:59:59'))]

        overNightHyperglycemiaAuto.append((len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 180]) / 288))

        overNightHyperglycemiaCriticalAuto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] > 250]) / 288))

        overNightInRangeAuto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / 288))

        overNightInRangeSecondaryAuto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / 288))

        overNightHypoglycemiaLevel1Auto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 70]) / 288))

        overNightHypoglycemiaLevel2Auto.append(
            (len(overNightFrame[overNightFrame['Sensor Glucose (mg/dL)'] < 54]) / 288))

        dayTimeHyperglycemiaAuto.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 180]) / 288))

        dayTimeHyperglycemiaCriticalAuto.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] > 250]) / 288))

        dayTimeInRangeAuto.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / 288))

        dayTimeInRangeSecondaryAuto.append(
            (len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / 288))

        dayTimeHypoglycemiaLevel1Auto.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 70]) / 288))

        dayTimeHypoglycemiaLevel2Auto.append((len(dayTimeFrame[dayTimeFrame['Sensor Glucose (mg/dL)'] < 54]) / 288))

        wholeDayHyperglycemiaAuto.append((len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 180]) / 288))

        wholeDayHyperglycemiaCriticalAuto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] > 250]) / 288))

        wholeDayInRangeAuto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 180, inclusive=True)]) / 288))

        wholeDayInRangeSecondaryAuto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'].between(70, 150, inclusive=True)]) / 288))

        wholeDayHypoglycemiaLevel1Auto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 70]) / 288))

        wholeDayHypoglycemiaLevel2Auto.append(
            (len(wholeDayFrame[wholeDayFrame['Sensor Glucose (mg/dL)'] < 54]) / 288))




print('overnight auto')
print((sum(overNightHyperglycemiaAuto) / autoModeDaysCount) * 100)

print((sum(overNightHyperglycemiaCriticalAuto) / autoModeDaysCount) * 100)

print((sum(overNightInRangeAuto) / autoModeDaysCount) * 100)

print((sum(overNightInRangeSecondaryAuto) / autoModeDaysCount) * 100)

print((sum(overNightHypoglycemiaLevel1Auto) / autoModeDaysCount) * 100)

print((sum(overNightHypoglycemiaLevel2Auto) / autoModeDaysCount) * 100)

print('dayTime auto')
print((sum(dayTimeHyperglycemiaAuto) / autoModeDaysCount) * 100)

print((sum(dayTimeHyperglycemiaCriticalAuto) / autoModeDaysCount) * 100)

print((sum(dayTimeInRangeAuto) / autoModeDaysCount) * 100)

print((sum(dayTimeInRangeSecondaryAuto) / autoModeDaysCount) * 100)

print((sum(dayTimeHypoglycemiaLevel1Auto) / autoModeDaysCount) * 100)

print((sum(dayTimeHypoglycemiaLevel2Auto) / autoModeDaysCount) * 100)

print('whole day auto')
print((sum(wholeDayHyperglycemiaAuto) / autoModeDaysCount) * 100)

print((sum(wholeDayHyperglycemiaCriticalAuto) / autoModeDaysCount) * 100)

print((sum(wholeDayInRangeAuto) / autoModeDaysCount) * 100)

print((sum(wholeDayInRangeSecondaryAuto) / autoModeDaysCount) * 100)

print((sum(wholeDayHypoglycemiaLevel1Auto) / autoModeDaysCount) * 100)

print((sum(wholeDayHypoglycemiaLevel2Auto) / autoModeDaysCount) * 100)

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


def output(listValue, daysCount):
    return round((sum(listValue) / daysCount) * 100, 2)


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
