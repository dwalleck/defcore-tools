import json

f = open('results.json')
data = f.read()

tests = json.loads(data)

details = open('test_request_details.md', 'w')
for k, v in tests.iteritems():
    test_name = k.split('[')[0]
    
    details.write(test_name + '\n')
    
    if v:
        for item in v:
            details.write('- ' + item.get('verb') + ' request for ' + item.get('service') + ' to ' + item.get('url') + '\n')
    details.write('\n')
