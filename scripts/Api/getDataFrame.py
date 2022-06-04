import datetime as dt
import pandas as pd
import requests

def get_df(url: str, params: dict, sample: bool = True):
        all_results = []
        current_page = 1
        total_pages = 1
        if sample: 
            while current_page <= 1:
                    tic = dt.datetime.now()
                    params["page"] = current_page
                    try:
                            r = requests.get(url, params)
                            all_results = all_results + r.json()["response"]["results"]
                            r.raise_for_status()
                    except Exception as err:
                            SystemExit(err)
                    if current_page == 1:
                            print("---- API STATUS ---- ")
                            print("status",  r.json()["response"]["status"])
                            total_pages = r.json()['response']['pages']
                            print("URL: ", r.url)
                            print("status",  r.json()["response"]["status"])
                            print("total",  r.json()["response"]["total"])
                            print("startIndex",  r.json()["response"]["startIndex"])
                            print("pageSize",  r.json()["response"]["pageSize"])
                            print("pages",  r.json()["response"]["pages"])
                            print("orderBy",  r.json()["response"]["orderBy"])
                            print("---- RUNTIME STATUS ---- ")

                    time_taken = str(dt.datetime.now() - tic)
                    print(f"({current_page}/{total_pages}) in {time_taken}s")
                            
                    current_page += 1
        else:
            while current_page <= total_pages:
                    tic = dt.datetime.now()
                    params["page"] = current_page
                    try:
                            r = requests.get(url, params)
                            all_results = all_results + r.json()["response"]["results"]
                            r.raise_for_status()
                    except Exception as err:
                            SystemExit(err)
                    if current_page == 1:
                            print("---- API STATUS ---- ")
                            print("status",  r.json()["response"]["status"])
                            total_pages = r.json()['response']['pages']
                            print("URL: ", r.url)
                            print("status",  r.json()["response"]["status"])
                            print("total",  r.json()["response"]["total"])
                            print("startIndex",  r.json()["response"]["startIndex"])
                            print("pageSize",  r.json()["response"]["pageSize"])
                            print("pages",  r.json()["response"]["pages"])
                            print("orderBy",  r.json()["response"]["orderBy"])
                            print("---- RUNTIME STATUS ---- ")

                    time_taken = str(dt.datetime.now() - tic)
                    print(f"({current_page}/{total_pages}) in {time_taken}s")
                            
                    current_page += 1

        return pd.DataFrame(all_results)