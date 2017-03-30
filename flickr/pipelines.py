# -*- coding: utf-8 -*-
import os


class FlickrPipeline(object):
    def process_item(self, item, spider):
        output_dir = 'images'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        filename = item['image_url'].split('/')[-1]
        with open(os.path.join(output_dir, filename), 'wb') as f:
            f.write(item['image_body'])

        return item
