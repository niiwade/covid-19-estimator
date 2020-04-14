## Challenge 1
def convertToDays(period_type, timeToElapse):
  if period_type == 'days':
    return timeToElapse

  elif period_type == 'weeks':
    return timeToElapse * 7

  elif period_type == 'months':
    return timeToElapse * 30

  else:
    return timeToElapse

period_type = input('Enter a period- days, weeks or months')
timeToElapse = int(input('Enter the number of days'))
reportedCases = int(input('Enter the number of reported cases'))
population = int(input('Population'))
totalHospitalBeds = int(input('Hospital beds'))
currentlyInfected = 0
infectionsByRequestedTime = 0

data: {

    'region':{

        'name': "Africa",
        'avgAge': 19.7,
        'avgDailyIncomeInUSD': 5,
        'avgDailyIncomePopulation': 0.71

    },

      'period_type' : "days",
      'timeToElapse' : 58,
      'reportedCases' : 674,
      'population' : 66622705,
      'totalHospitalBeds' : 1380614
    
}

data ['timeToElapse'] = convertToDays(data['periodType'], data['timeToElapse'])

dataOutput = {

    'data' : data,

    'impact' : {
      'currentlyInfected' : data['reportedCases'] * 10,
    },

    'severeImpact' : {
      'currentlyInfected' : data['reportedCases'] * 50,
    }

  }

def estimator(data):

    days = 2 ** int((data['timeToElapse']/3))
    beds = int(dataOutput['data']['totalHospitalBeds'] * 0.35)

    dataOutput['impact']['infectionsByRequestedTime'] = dataOutput['impact']['currentlyInfected'] * days
    dataOutput['severeImpact']['infectionsByRequestedTime'] = dataOutput['severeImpact']['currentlyInfected'] * days
    dataOutput['impact']['severeCasesByRequestedTime'] = dataOutput['impact']['infectionsByRequestedTime'] * 0.15
    dataOutput['severeImpact']['severeCasesByRequestedTime'] = dataOutput['severeImpact']['infectionsByRequestedTime'] * 0.15
    dataOutput['impact']['hospitalBedsByRequestedTime'] =  beds - dataOutput['impact']['severeCasesByRequestedTime']
    dataOutput['severeImpact']['hospitalBedsByRequestedTime'] = beds - dataOutput['severeImpact']['severeCasesByRequestedTime']
    dataOutput['impact']['casesForICUByRequestedTime'] =int(round(dataOutput['impact']['infectionsByRequestedTime'] * (5/100), 2))
    dataOutput['severeImpact']['casesForICUByRequestedTime'] = int(round(dataOutput['severeImpact']['infectionsByRequestedTime'] * (5/100), 2))
    dataOutput['impact']['casesForVentilatorsByRequestedTime'] = int(round(dataOutput['impact']['infectionsByRequestedTime'] * (2/100), 2))
    dataOutput['severeImpact']['casesForVentilatorsByRequestedTime'] = int(round(dataOutput['severeImpact']['infectionsByRequestedTime'] * (2/100), 2))
    dataOutput['impact']['dollarsInFlight'] = int((dataOutput['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])
    dataOutput['severeImpact']['dollarsInFlight'] = int((dataOutput['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation']) * data['region']['avgDailyIncomeInUSD'] * data['timeToElapse'])

    return dataOutput

print (estimator(data))

