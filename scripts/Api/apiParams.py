
import os

params = {
    "page-size": "50",
    "show-fields": 
            "all"
    #    "trailText,headline,body,wordcount,firstPublicationDate,productionOffice,charCount,commentable,starRating,isLive, lastModified,Score,commentCloseDate"
    ,
    "show-elements": "all",
    "show-tags": ["all"],
    "show-rights": "syndicatable",
    "order-by": "newest",
    "api-key": os.getenv("GUARDIAN_API_KEY"),
}

