class Card:
    name = "card name"
    full_name = "full card name"
    image_path = "image path"
    power = -1  # zastąpi głupie metody get card number!

    image_id = -1 # index of the image in the card_images list

    def __init__(self, name, full_name, image_path, power):
        self.name = name
        self.full_name = full_name
        self.image_path = image_path
        self.power = power

    def get_name(self):
        return self.name

    def get_full_name(self):
        return self.full_name

    def get_power(self):
        return self.power

    def get_image_path(self):
        return self.image_path

    def set_image_id(self, image_id):
        self.image_id = image_id

    def get_image_id(self):
        return self.image_id



    #where it belongs? to what collection in logic?

    #where it belongs on the gui label colleciton?
    # label object