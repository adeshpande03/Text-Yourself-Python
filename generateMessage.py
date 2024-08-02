import requests
import json
from pprint import *
import json
from datetime import datetime, timezone


def getWeather():
    url = "https://api.weatherapi.com/v1/current.json?key=d0feacb41e1345dcb66203126241502&q=Austin&aqi=no"
    data = requests.get(url).content
    data = json.loads(data)
    current = data["current"]
    # pprint(data)
    message = f"Rain {current['precip_in']} in Temp {current['temp_f']}F, feels like {current['feelslike_f']}F, Wind {current['wind_dir']} at {current['wind_mph']} mph."
    # print(message)
    return message


def isUnixToday(unix_time):
    unix_time = int(unix_time)
    date_from_unix = datetime.fromtimestamp(unix_time, tz=timezone.utc)
    today_date = datetime.now(timezone.utc)
    return (
        date_from_unix.year == today_date.year
        and date_from_unix.month == today_date.month
        and date_from_unix.day == today_date.day
    )


def getLeetCode():
    username = "impgriffin"
    url = "https://leetcode.com/graphql"
    headers = {"Content-Type": "application/json", "Referer": "https://leetcode.com"}

    query = """
    query getUserProfile($username: String!) {
        activeDailyCodingChallengeQuestion {
		date
		userStatus
		link
		question {
			acRate
			difficulty
			freqBar
			frontendQuestionId: questionFrontendId
			isFavor
			paidOnly: isPaidOnly
			status
			title
			titleSlug
			hasVideoSolution
			hasSolution
			topicTags {
				name
				id
				slug
			}
		}
	}
        # allQuestionsCount {
        #   difficulty
        #   count
        # }
        matchedUser(username: $username) {
          contributions {
            points
          }
        #   profile {
        #     reputation
        #     ranking
        #   }
        #   submissionCalendar
        #   submitStats {
        #     acSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #     }
        #     totalSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #     }
        #   }
        }
        recentSubmissionList(username: $username) {
          title
          titleSlug
          timestamp
          statusDisplay
          lang
          __typename
        }
        # matchedUserStats: matchedUser(username: $username) {
        #   submitStats: submitStatsGlobal {
        #     acSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #       __typename
        #     }
        #     totalSubmissionNum {
        #       difficulty
        #       count
        #       submissions
        #       __typename
        #     }
        #     __typename
        #   }
        # }
        
      }
    """

    variables = {"username": username}
    response = requests.post(
        url, headers=headers, json={"query": query, "variables": variables}
    )
    content = response.json()
    current_coins = content["data"]["matchedUser"]["contributions"]["points"]
    recent_subs = content["data"]["recentSubmissionList"]
    daily = content["data"]["activeDailyCodingChallengeQuestion"]["question"][
        "titleSlug"
    ]
    # pprint(daily)
    daily_done = False
    for sub in recent_subs:
        if isUnixToday(sub["timestamp"]) and sub["titleSlug"] == daily:
            daily_done = True
    # print(daily_done, current_coins)
    # if response.status_code == 200:
    #     return response.json()  # Returns the JSON response from the API
    # else:
    #     return {'error': 'Failed to fetch data', 'status_code': response.status_code}
    return f"Your daily problem is {'done' if daily_done else 'not done'}, and you currently have {current_coins} LeetCoins!"


def generateMessage():
    weather = getWeather()
    leetcode = getLeetCode()
    message = [
        # weather,
        leetcode
    ]
    # pprint(message)
    return message


if __name__ == "__main__":
    generateMessage()
