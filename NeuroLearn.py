from pathlib import Path

# Location of the downloaded dataset
dataset_path = Path("..")

# Find every MRI image inside the dataset
image_files = (
    list(dataset_path.rglob("*.jpg"))
    + list(dataset_path.rglob("*.jpeg"))
    + list(dataset_path.rglob("*.png"))
)

print(f"Number of images found: {len(image_files)}")

import random
from PIL import Image
import matplotlib.pyplot as plt

score = 0
attempts = 0
def reveal(guess):
    global score, attempts

    attempts += 1

    guess = guess.lower().replace(" ", "")

    if guess == actual_label:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Not quite!")

    print(f"Actual class: {actual_label}")
    print(f"Score: {score}/{attempts}")

def mystery_mri():
    global current_image, actual_label

    current_image = random.choice(image_files)
    actual_label = current_image.parent.name.lower()

    image = Image.open(current_image)

    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.title("Mystery MRI")
    plt.show(block=False)
    plt.pause(0.5)

    guess = input(
        "Your guess (glioma, meningioma, pituitary, notumor): "
    )

    reveal(guess)
    plt.close()

    guess = input(
        "Your guess (glioma, meningioma, pituitary, notumor): "
    )

    reveal(guess)
    plt.close()


mystery_mri()


