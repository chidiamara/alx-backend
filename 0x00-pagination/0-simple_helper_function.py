#!/usr/bin/env python3
"""Helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """_summary_

    Args:
        page (int): _description_
        page_size (int): _description_

    Returns:
        Tuple[int, int]: _description_
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
