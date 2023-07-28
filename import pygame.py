import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

def stop_music():
    pygame.mixer.music.stop()

def main():
    print("Welcome to the Python Music Player!")
    print("1. Play Music")
    print("2. Pause Music")
    print("3. Unpause Music")
    print("4. Stop Music")
    print("5. Exit")

    while True:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            file_path = input("Enter the path to the music file: ")
            if not os.path.exists(file_path):
                print("File not found!")
                continue
            play_music(file_path)
        elif choice == 2:
            pause_music()
        elif choice == 3:
            unpause_music()
        elif choice == 4:
            stop_music()
        elif choice == 5:
            stop_music()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


















































































