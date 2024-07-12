import json

with open("../GetDataFromAPI/GetDataFromAPI/matches.json", "r", encoding="utf-8") as file:
    text = file.read()
    json_dict = json.loads(text)
    matches = json_dict["matches"]

results_matches = []

for match in matches:
    match_result = dict()
    match_result["name_country"] = match["area"]["name"]
    match_result["name_competition"] = match["competition"]["name"]
    match_result["start_season"] = match["season"]["startDate"]
    match_result["end_season"] = match["season"]["endDate"]
    match_result["matchday"] = match["season"]["currentMatchday"]
    match_result["utc_date"] = match["utcDate"]
    match_result["home_team_name"] = match["homeTeam"]["name"]
    match_result["home_team_sh_name"] = match["homeTeam"]["shortName"]
    match_result["away_team_name"] = match["awayTeam"]["name"]
    match_result["away_team_sh_name"] = match["awayTeam"]["shortName"]
    match_result["name_winner"] = match["score"]["winner"]
    match_result["points_fulltime_home"] = match["score"]["fullTime"]["home"]
    match_result["points_fulltime_away"] = match["score"]["fullTime"]["away"]
    match_result["points_halftime_home"] = match["score"]["halfTime"]["home"]
    match_result["points_halftime_away"] = match["score"]["halfTime"]["away"]
    results_matches.append(match_result)












#"matches": [{ "area":{"name":},
# "competition": {"name":},
# "season": {"startDate":, "endDate":, "currentMatchday":},
# "utcDate":,
# "homeTeam": {"name":, "shortName":},
# "awayTeam": {"name":, "shortName":},
# "score": {"winner":,
# "fullTime": {"home":,"away":},
# "halfTime": {"home":,"away":}]

