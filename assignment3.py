import argparse
import urllib.request
import re
import datetime
import csv
import io
import pprint


def downloadData(url):
    
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def process_data(urldata):
   
    browser_count = {
        "MSIE": 0,
        "Safari": 0,
        "Chrome": 0,
        "Firefox": 0
    }
    hours_accessed = {hour: 0 for hour in range(24)}
    csv_data = csv.reader(io.StringIO(urldata))
    image_counter = 0
    total_hits = 0
    percent_image_hits = 0

    for row in csv_data:
        path_to_file = row[0]
        datetime_access_str = row[1]
        browser = row[2]
        # GIF, JPG, JPEG, PNG
        # Try to do this with a regular expression
        if re.search(r"\.JPG|\.JPEG|\.GIF|\.PNG", path_to_file, re.IGNORECASE):
            image_counter = image_counter + 1
        total_hits += 1

        if re.search(r"MSIE",browser, re.IGNORECASE):
            browser_count["MSIE"] += 1
        if re.search(r"Safari",browser, re.IGNORECASE):
            browser_count["Safari"] += 1
        if re.search(r"Chrome",browser, re.IGNORECASE):
            browser_count["Chrome"] += 1
        if re.search(r"Firefox",browser, re.IGNORECASE):
            browser_count["Firefox"] += 1


    
        access_time = datetime.datetime.strptime(datetime_access_str, "%Y-%m-%d %H:%M:%S")
        hours_accessed[access_time.hour] += 1
    percent_image_hits = (image_counter / total_hits) * 100


    
    print(f"Image requests account for {percent_image_hits}% of all requests.")
    
    print(f"The most popular browser is {max(browser_count)}")

    most_popular_browser = max(browser_count, key=browser_count.get)

    for hour, count in sorted(hours_accessed.items(), key=lambda x: x[1], reverse=True):
        print(f"Hour {hour} has {count} hits")

def main(url):
    data = downloadData(url)
    process_data(data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)