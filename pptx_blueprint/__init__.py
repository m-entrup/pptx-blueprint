import pathlib
import pptx
from typing import Union, Iterable
from pptx.shapes.base import BaseShape

_Pathlike = Union[str, pathlib.Path]


class Template:
    """Helper class for modifying pptx templates.
    """

    def __init__(self, filename: _Pathlike) -> None:
        """Initializes a Template-Modifier.

        Args:
            filename (path-like): file name or path
        """
        self._template_path = filename
        self._presentation = pptx.Presentation(filename)
        pass

    def replace_text(self, label: str, text: str, *, scope=None) -> None:
        """Replaces text placeholders on one or many slides.

        Args:
            label (str): label of the placeholder (without curly braces)
            text (str): new content
            scope: None, slide number, Slide object or iterable of Slide objects
        """
        pass

    def replace_picture(self, label: str, filename: _Pathlike, *, do_not_scale_up: bool = False) -> None:
        """Replaces rectangle placeholders on one or many slides.

        Args:
            label (str): label of the placeholder (without curly braces)
            filename (path-like): path to an image file
            do_not_scale_up (bool): deactivates that the image is enlarged (default: False)
        """
        shapes_to_replace = self._find_shapes(label)
        if not shapes_to_replace:
            return
        if isinstance(filename, str):
            filename = pathlib.Path(filename)
        if not filename.is_file():
            raise FileNotFoundError(f"The file does not exist: {filename}")
        img_file = open(filename, "rb")
        old_shape: BaseShape
        for old_shape in shapes_to_replace:
            slide_shapes = old_shape._parent
            img_shape = slide_shapes.add_picture(
                image_file=img_file,
                left=old_shape.left,
                top=old_shape.top,
            )
            # Scaling the image if `do_not_scale == False`:
            if img_shape.height <= old_shape.height and img_shape.width <= old_shape.width and not do_not_scale_up:
                old_aspect_ratio = old_shape.width / old_shape.height
                new_aspect_ratio = img_shape.width / img_shape.height
                if old_aspect_ratio >= new_aspect_ratio:
                    img_shape.width = old_shape.width
                    img_shape.height = int(img_shape.width / new_aspect_ratio)
                else:
                    img_shape.height = old_shape.height
                    img_shape.width = int(img_shape.height * new_aspect_ratio)
            # Centering the image at the extent of the placeholder:
            img_shape.top += int((old_shape.height - img_shape.height) / 2)
            img_shape.left += int((old_shape.width - img_shape.width) / 2)
            del slide_shapes[slide_shapes.index(old_shape)]
            # Removing shapes is performed at the lxml level.
            # The `element` attribute contains an instance of `lxml.etree._Element`.
            slide_shapes.element.remove(old_shape.element)

    def replace_table(self, label: str, data) -> None:
        """Replaces rectangle placeholders on one or many slides.

        Args:
            label (str): label of the placeholder (without curly braces)
            data (pandas.DataFrame): table to be inserted into the presentation
        """
        pass

    def _find_shapes(self, label: str) -> Iterable[BaseShape]:
        """ Finds all shapes that match the label

        Args:
            label (str): label of the placeholder (without curly braces)
        """
        pass

    def save(self, filename: _Pathlike) -> None:
        """Saves the updated pptx to the specified filepath.

        Args:
            filename (path-like): file name or path
        """
        # TODO: make sure that the user does not override the self._template_path
        pass
