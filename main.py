from scene_startmenu import SceneStartMenu
from scene_gameplay import SceneGameplay


def main():

    scene_1 = SceneStartMenu()
    while scene_1.is_running:
        scene_1.run()
        scene_1.end()

    scene_2 = SceneGameplay()
    while True:
        scene_2.run()


if __name__ == "__main__":
    main()
