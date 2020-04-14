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
    dataOutput['impact']['dollarsInFlight'] = int((dataOutput['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / data['timeToElapse'])
    dataOutput['severeImpact']['dollarsInFlight'] = int((dataOutput['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / data['timeToElapse'])

    return dataOutput

print (estimator(data))




  #calculate the number of days

def number_of_days(periodtype, time_to_elapse):
    if periodtype == 'days':
        days = time_to_elapse

    elif period_type == 'weeks':
        days = time_to_elapse * 7

    elif periodtype == 'months':
      days = time_to_elapse * 30

    return days

  #infections by requested time, where case = currentlyInfected
def infected_till_date(case):
    days = number_of_days(periodtype, time_to_elapse) // 3
    return case * (2 ** days)

def severe_by_req_time(case):
    return 0.15 * infected_till_date(case)

def hospital_bedsby_time(case):
    return int(available_beds - severe_by_req_time(case))

def money_lost(case):
    inf = infected_till_date(case)
    days = number_of_days(periodtype, time_to_elapse)
    return int((inf * income_population * income) / days)
    
tt = {
        
        "region": {
            "name": "Africa",
            "avgAge": 19.7,
            "avgDailyIncomeInUSD": 4,
            "avgDailyIncomePopulation": 0.73
        },
        "periodType": "days",
        "timeToElapse": 38,
        "reportedCases": 2747,
        "population": 92931687,
        "totalHospitalBeds": 678874
    }



result = {
    "data":data,
    "impact": {
    "currentlyInfected": impact_cases,
        "infectionsByRequestedTime": infected_till_date(impact_cases),
        "severeCasesByRequestedTime": int(severe_by_req_time(impact_cases)),
        "hospitalBedsByRequestedTime": hospital_bedsby_time(impact_cases),
        "casesForICUByRequestedTime": int(0.05 * infected_till_date(impact_cases)),
        "casesForVentilatorsByRequestedTime":int(0.02 * infected_till_date(impact_cases)),
        "dollarsInFlight": money_lost(impact_cases)
        },
        "severeImpact": {
        "currentlyInfected": severe_cases,
        "infectionsByRequestedTime": infected_till_date(severe_cases),
        "severeCasesByRequestedTime": int(severe_by_req_time(severe_cases)),
        "hospitalBedsByRequestedTime": hospital_bedsby_time(severe_cases),
        "casesForICUByRequestedTime": int(0.05 * infected_till_date(severe_cases)),
        "casesForVentilatorsByRequestedTime": int(0.02 * infected_till_date(severe_cases)),
        "dollarsInFlight": money_lost(severe_cases)
        }
}

return result

    #test
 

print(estimator(tt)) 