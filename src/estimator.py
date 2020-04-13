def test_challenge1():
          for [period_type, challenge] in cases:
            loop = asyncio.get_event_loop()
            input = loop.run_until_complete(
                test_utils.mock_estimation_for(period_type))
        
            # nodes from end point
            data = input["data"]
            estimate = input["estimate"]
        
            output = estimator(data)
    >       values = test_utils.value_on_fields(output, estimate, challenge)
