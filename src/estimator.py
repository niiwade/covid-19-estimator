## Challenge 1
def convertToDays(period_type, timeToElapse):
  if period_type == 'days':
    return timeToElapse

  elif period_type == 'weeks':
    return timeToElapse * 7

  elif period_type == 'months':
    return timeToElapse * 30

  else:
    return 'Incorrect input'

period_type = input('Enter a period- days, weeks or months')
timeToElapse = int(input('Enter the number of days'))
reportedCases = int(input('Enter the number of reported cases'))
population = int(input('Population'))
totalHospitalBeds = int(input('Hospital beds'))
currentlyInfected = 0
infectionsByRequestedTime = 0

dataInput: {

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

dataInput ['timeToElapse'] = convertToDays(dataInput['periodType'], dataInput['timeToElapse'])

data = {

    'data' : dataInput,

    'impact' : {
      'currentlyInfected' : dataInput['reportedCases'] * 10,
    },

    'severeImpact' : {
      'currentlyInfected' : dataInput['reportedCases'] * 50,
    }

  }


data['impact']['infectionsByRequestedTime'] = data['impact']['currentlyInfected'] * (2 ** (timeToElapse/3))
data['severeImpact']['infectionsByRequestedTime'] = data['severeImpact']['currentlyInfected'] * (2 ** (timeToElapse/3))
data['impact']['severeCasesByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (15/100)
data['severeImpact']['severeCasesByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (15/100)
data['impact']['hospitalBedsByRequestedTime'] = data['impact']['severeCasesByRequestedTime'] - data['data']['totalHospitalBeds']
data['severeImpact']['hospitalBedsByRequestedTime'] = data['severeImpact']['severeCasesByRequestedTime'] - data['data']['totalHospitalBeds']
data['impact']['casesForICUByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (5/100)
data['severeImpact']['casesForICUByRequestedTime'] = data['severeImpact']['infectionsByRequestedTime'] * (5/100)
data['impact']['casesForVentilatorsByRequestedTime'] = data['impact']['infectionsByRequestedTime'] * (2/100)
data['severeImpact']['casesForVentilatorsByRequestedTime'] = data['severeImpact']['infectionsByRequestedTime'] * (2/100)



def estimator(data):

  return data

print(estimator(data)) 
