import os


def get_image_path(instance, filename):
    category_name = instance.category_id.category_name if instance.category_id else "misc"
    return os.path.join('product_images', category_name, filename)
