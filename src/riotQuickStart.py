from riotwatcher import LolWatcher
import pandas as pd

#
# riotQuickStart.py  - provides demonstration of the use of Riot Games remote API's via the riot watcher Python wrapper.
# Note: use the Riot Games site to see the up to date definitions of DTO (data transfer objects) referenced below.
# https://developer.riotgames.com/apis
#

#
# Convenience debugging functions
#
debugOutput = False


def print_summoner_dto(summoner_dto):
    print("Summoner name: " + summoner_dto['name'])
    print("\tpuuid: " + summoner_dto['puuid'])
    print("\taccountId: " + summoner_dto['accountId'])
    print("\tprofileIconId: " + str(summoner_dto['profileIconId']))
    print("\trevisionDate: " + str(summoner_dto['revisionDate']))
    print("\tid " + summoner_dto['id'])
    print("\tsummonerLevel: " + str(summoner_dto['summonerLevel']))


def print_participant_dtos(match_id, participant_dtos):
    print("\n\n\t\tMatch ID: " + match_id)
    participants = []
    for row in participant_dtos:
        if debugOutput:
            print(row)
        participants_row = {}
        participants_row['assists'] = row['assists']
        participants_row['baronKills'] = row['baronKills']
        participants_row['championName'] = row['championName']
        participants_row['perks-defense'] = row['perks']['statPerks']['defense']
        participants.append(participants_row)

    df = pd.DataFrame(participants)
    print(df)


# The region to execute the Summoner request on.
my_region = 'na1'

# The region to execute the Match request on. Underlying API uses this in the endpoint URL.
my_region2 = 'americas'

#  The named summoner we will use the SummonerApiV4 class to retrieve a SummonerDTO.
summonerName = 'Doublelift'

# Riot Games API key. Valid for 24 hours only and then must be regenerated.
# Requires a Riot Games dev account. Note: see other usage limitations.
riotGamesApiKey = 'RGAPI-120a1779-37cd-47a1-a8f6-4feb8fef6428'

#
# LolWatcher class is the main interaction point with the APIs for League of Legends.
# It provides access to SummonerApiV4, MatchApiV5 classes and others.
#

# Instantiate the riot watcher main class based on the Riot Games API key.
# Retrieve the summoner dto (data transfer object) interface.
watcher = LolWatcher(riotGamesApiKey)
summonerDto = watcher.summoner.by_name(my_region, summonerName)

if debugOutput:
    print_summoner_dto(summonerDto)

# Use the MatchApiV5 class to retrieve a list of match ids  for a given summoner puuid
matchIdList = watcher.match.matchlist_by_puuid(my_region2, summonerDto['puuid'])

if debugOutput:
    print(matchIdList)

#
# Do a formatted output using the pandas package
#
print("\n\nMatch report for Summoner \'" + summonerName + "\'. Number of matches : " + str(len(matchIdList)))

for matchId in matchIdList:
    # Retrieve a single match details given a match id.
    # The match dto contains a MetadataDto and a InfoDto.
    matchDto = watcher.match.by_id(my_region2, matchId)
    matchMetadataDto = matchDto['metadata']
    matchInfoDto = matchDto['info']
    matchParticipantDtos = matchInfoDto['participants']

    print_participant_dtos(matchMetadataDto['matchId'], matchParticipantDtos)
