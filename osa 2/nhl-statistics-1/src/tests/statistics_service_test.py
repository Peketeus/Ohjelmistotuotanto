import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    # nimi, tiimi, maalit, avustukset
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
    # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_konstruktori_saa_pelaajat(self):
        players = self.stats._players
        self.assertEqual(len(players), 5)

    def test_search_palauttaa_pelaajan_tiedot(self):
        searched_player = self.stats.search("Kurri")
        self.assertEqual(searched_player.name, "Kurri")
        self.assertEqual(searched_player.team, "EDM")
        self.assertEqual(searched_player.goals, 37)
        self.assertEqual(searched_player.assists, 53)

    def test_search_palauttaa_none(self):
        searched_player = self.stats.search("Granlund")
        self.assertIsNone(searched_player)

    def test_team_palauttaa_pelaajat(self):
        searched_team = self.stats.team("EDM")
        self.assertEqual(len(searched_team), 3)
        names = []

        for player in searched_team:
            names.append(player.name)

        self.assertEqual(names, ["Semenko", "Kurri", "Gretzky"])
        
    def test_top_palauttaa_parhaat_pelaajat(self):
        searched_top = self.stats.top(2)
        names = []

        for player in searched_top:
            names.append(player.name)

        self.assertEqual(names, ["Gretzky", "Lemieux", "Yzerman"])