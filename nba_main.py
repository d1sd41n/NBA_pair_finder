#!/usr/bin/python
import json
import sys
import urllib.request


class GetData:
    def get_data(self, url):
        """[Gets data from an endpoint]

        Args:
            url ([str]): [endpoint's url]

        Returns:
            [byte str]: [data from the endpoint]
        """
        response = urllib.request.urlopen(url)

        return response.read()


class Bytes2Dict:
    def data_2_dict(self, data):
        """[convetrs Byte str JSON to dict]

        Args:
            data ([byte str]): [description]

        Returns:
            [dict]: [data in a dict]
        """
        data_str = data.decode("UTF-8")
        return json.loads(data_str)


class GetNBAplayersList:

    def get_list(self, url):
        """[Gets NBA players list]

        Args:
            url ([str]): [data]

        Returns:
            [list]: [NBA players list]
        """
        b_data = GetData().get_data(url)
        d_data = Bytes2Dict().data_2_dict(b_data)

        return d_data["values"]


def get_player_pairs(nba_data, sum_n):
    """[find pairs of NBA players by the sum of their heights]

    Args:
        nba_data ([list]): [NBA player list]
        sum_n ([type]): [number used in the search,
            the sum of the height of the players
            must give this number]

    Returns:
        [list]: [names of the pairs of players]
    """
    pairs = []
    hash_table = {}

    for i in range(len(nba_data)):

        number = int(nba_data[i]["h_in"])
        name = f"{nba_data[i]['first_name']} {nba_data[i]['last_name']}"

        if not number in hash_table:
            hash_table[number] = [name]
        else:
            hash_table[number].append(name)

    for i in range(len(nba_data)):
        sub = sum_n - int(nba_data[i]["h_in"])

        if sub in hash_table:
                
            name = f"{nba_data[i]['first_name']} {nba_data[i]['last_name']}"
            name2 = hash_table[sub].pop()

            if name != name2:
                pairs.append((name, name2))

            if not hash_table[sub]:
                del hash_table[sub]

    return pairs


def print_pairs(nba_pairs):

    print("")

    if nba_pairs:
        for x in nba_pairs:
            print(f"-{x[0]}  {x[1]}")
    else:
        print("No matches found")


class NBAPairFinder:
    nba_url = "https://mach-eight.uc.r.appspot.com/"

    def find_pair(self, sum_n):

        nba_data = GetNBAplayersList().get_list(self.nba_url)
        nba_pairs = get_player_pairs(nba_data, sum_n)

        print_pairs(nba_pairs)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise Exception("Please enter an argument")
    elif not sys.argv[1].isnumeric():
        raise Exception("The argument must be numeric")

    sum = int(sys.argv[1])

    NBAPairFinder().find_pair(sum)
