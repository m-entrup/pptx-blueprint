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

    def replace_picture(self, label: str, filename: _Pathlike) -> None:
        """Replaces rectangle placeholders on one or many slides.

        Args:
            label (str): label of the placeholder (without curly braces)
            filename (path-like): path to an image file
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
            slide_shapes.add_picture(
                image_file=img_file,
                left=old_shape.left,
                top=old_shape.top,
                width=old_shape.width,
                height=old_shape.height
            )
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
