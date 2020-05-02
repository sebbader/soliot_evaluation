import requests
import urllib3
import time
from datetime import datetime
import sys


def execute_http_requests(serverType, runNr):
    http_urls = []
    http_unsafe_urls = []
    http_times = []

    if serverType == 'soliot':
        with open("http_uris_soliot.txt", 'r') as f:
            for url in f.readlines():
                http_urls.append(url.strip())
        
        with open("http_unsafe_uris_soliot.txt", 'r') as f:
            for url in f.readlines():
                http_unsafe_urls.append(url.strip())
    else:
        with open("http_uris_solid.txt", 'r') as f:
            for url in f.readlines():
                http_urls.append(url.strip())
        
        with open("http_unsafe_uris_solid.txt", 'r') as f:
            for url in f.readlines():
                http_unsafe_urls.append(url.strip())

    urllib3.disable_warnings()

    for url in http_urls:
        start = time.perf_counter()
        try:
            response = requests.get(url, verify=False, stream=True)
            raw_content = response.raw.read()
            stop = time.perf_counter()
            current_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            http_times.append({'code': response.status_code, 'diff': int(round(stop - start, 3) * 1000), 'length': len(raw_content), 'datetime': current_time, 'uri': url, 'method': 'get', 'serverType': serverType})
            print(stop - start)
        except Exception as e:
            print(e)
    

    data = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> . @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>. @prefix sosa: <http://www.w3.org/ns/sosa/> . @prefix ssn: <http://www.w3.org/ns/ssn/> . @prefix xsd: <http://www.w3.org/2001/XMLSchema#> . @prefix cdt: <http://w3id.org/lindt/custom_datatypes#> . @prefix idsSensor: <http://www.iml.fraunhofer.de/ids/sensor#> .         <./> rdf:type sosa:Result ;     sosa:isResultOf <120636/2020-10-24T01:22:30.866Z> ;     sosa:hasSimpleResult \"42 Cel\"^^cdt:ucum ."

    for url in http_unsafe_urls:
        # -- BEGIN Block 1: POST-GET-DELETE --
        
        # POST
        # creates unsafeTest.ttl
        start = time.perf_counter()
        try:
            headers = {
                'Content-Type': 'text/turtle',
                'Link': '<http://www.w3.org/ns/ldp#Resource>; rel="type"',
                'Slug': 'unsafeTest{}'.format(runNr)
            }
            response = requests.post(url, verify=False, stream=True, headers=headers, data=data)
            raw_content = response.raw.read()
            stop = time.perf_counter()
            current_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            http_times.append({'code': response.status_code, 'diff': int(round(stop - start, 3) * 1000), 'length': len(raw_content), 'datetime': current_time, 'uri': url, 'method': 'post', 'serverType': serverType})
            print(stop - start)
        except Exception as e:
            print(e)

        # GET
        start = time.perf_counter()
        try:
            response = requests.get(url + "unsafeTest{}.ttl".format(runNr), verify=False, stream=True)
            raw_content = response.raw.read()
            stop = time.perf_counter()
            current_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            http_times.append({'code': response.status_code, 'diff': int(round(stop - start, 3) * 1000), 'length': len(raw_content), 'datetime': current_time, 'uri': url + "unsafeTest{}.ttl".format(runNr), 'method': 'get', 'serverType': serverType})
            print(stop - start)
        except Exception as e:
            print(e)

        # DELETE
        start = time.perf_counter()
        try:
            response = requests.delete(url + "unsafeTest{}.ttl".format(runNr), verify=False, stream=True)
            raw_content = response.raw.read()
            stop = time.perf_counter()
            current_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            http_times.append({'code': response.status_code, 'diff': int(round(stop - start, 3) * 1000), 'length': len(raw_content), 'datetime': current_time, 'uri': url + "unsafeTest{}.ttl".format(runNr), 'method': 'delete', 'serverType': serverType})
            print(stop - start)
        except Exception as e:
            print(e)
        
        # -- END Block 1 --
        # -- BEGIN Block 2 PUT-GET-DELETE --

        # PUT
        # creates unsafeTest$.ttl
        start = time.perf_counter()
        try:
            headers = {
                'Content-Type': 'text/turtle',
                'Link': '<http://www.w3.org/ns/ldp#Resource>; rel="type"',
                'Slug': 'unsafeTest{}'.format(runNr)
            }
            response = requests.put(url + "unsafeTest{}".format(runNr), verify=False, stream=True, headers=headers, data=data)
            raw_content = response.raw.read()
            stop = time.perf_counter()
            current_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            http_times.append({'code': response.status_code, 'diff': int(round(stop - start, 3) * 1000), 'length': len(raw_content), 'datetime': current_time, 'uri': url + "unsafeTest{}".format(runNr), 'method': 'put', 'serverType': serverType})
            print(stop - start)
        except Exception as e:
            print(e)

        # GET
        start = time.perf_counter()
        try:
            response = requests.get(url + "unsafeTest{}".format(runNr), verify=False, stream=True)
            raw_content = response.raw.read()
            stop = time.perf_counter()
            current_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            http_times.append({'code': response.status_code, 'diff': int(round(stop - start, 3) * 1000), 'length': len(raw_content), 'datetime': current_time, 'uri': url + "unsafeTest{}".format(runNr), 'method': 'get', 'serverType': serverType})
            print(stop - start)
        except Exception as e:
            print(e)

        # DELETE
        start = time.perf_counter()
        try:
            response = requests.delete(url + "unsafeTest{}".format(runNr), verify=False, stream=True)
            raw_content = response.raw.read()
            stop = time.perf_counter()
            current_time = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            http_times.append({'code': response.status_code, 'diff': int(round(stop - start, 3) * 1000), 'length': len(raw_content), 'datetime': current_time, 'uri': url + "unsafeTest{}".format(runNr), 'method': 'delete', 'serverType': serverType})
            print(stop - start)
        except Exception as e:
            print(e)
        
    log_response_times("{}_http-log-{}.txt".format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), runNr), http_times)


def log_response_times(filename, times):
    with open("http_logs/" + filename, "w") as f:
        f.write("code, time total, length, date, time, uri, method, serverType\n")
        for j in range(len(times)):
            f.write("{}, {}, {}, {}, {}, {}, {}\n".format(times[j]['code'], times[j]['diff'], times[j]['length'], times[j]['datetime'], times[j]['uri'], times[j]['method'], times[j]['serverType']))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i in range(100):
            execute_http_requests('solid', "{}{}".format(i, sys.argv[1]))
            execute_http_requests('soliot', "{}{}".format(i, sys.argv[1]))
    else:    
        for i in range(100):
            execute_http_requests('solid', i)
            execute_http_requests('soliot', i)
