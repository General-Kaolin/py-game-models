import init_django_orm  # noqa: F401

import json
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file:
        data = json.load(file)

    for player_nickname, player_info in data.items():

        race_obj, _ = Race.objects.get_or_create(
            name=player_info["race"]["name"],
            defaults={"description": player_info["race"]["description"]}
        )

        for skills in player_info["race"]["skills"]:
            skill_obj, _ = Skill.objects.get_or_create(
                name=skills["name"],
                defaults={
                    "bonus": skills["bonus"],
                    "race": race_obj
                }
            )

        if player_info["guild"]:
            guild_obj, _ = Guild.objects.get_or_create(
                name=player_info["guild"]["name"],
                defaults={"description": player_info["guild"]["description"]}
            )
        else:
            guild_obj = None

        Player.objects.create(
            nickname=player_nickname,
            email=player_info["email"],
            bio=player_info["bio"],
            race=race_obj,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
