import torch
import numpy as np


def reshape_to_vectors(data: torch.Tensor) -> torch.Tensor:
    """
    Reshape the data to a 2D array of shape (N, D) where N is the number
    of data points and D is the dimensionality of each data point.

    Args:
        data (numpy.ndarray): The data to be reshaped of shape (N, D1, D2, ..., Dk).

    Returns:
        numpy.ndarray: The reshaped data of shape (N, D1 * D2 * ... * Dk).
    """

    reshaped_data = torch.zeros_like(data)

    # ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ Assignment 2.1 ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰ #
    # TODO:                                                             #
    # Implement the function that reshapes the data to a 2D array of    #
    # shape (N, D) where N is the number of data points and D is the    #
    # dimensionality of each data point.                                #
    #                                                                   #
    # Hint: Use the reshape function from numpy.                        #
    # Good luck!                                                        #
    # ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰ #
    # 🌀 INCEPTION 🌀 (Your code begins its journey here. 🚀 Do not delete this line.)

    reshaped_data = data.reshape(data.shape[0], -1)

    # 🌀 TERMINATION 🌀 (Your code reaches its end. 🏁 Do not delete this line.)

    return reshaped_data


def normalize_data(data: torch.Tensor) -> torch.Tensor:
    """
    Normalize the data to have zero mean and unit variance.
    The normalization is done over the first dimension.

    Args:
        data (numpy.ndarray): The data to be normalized of shape (N, D).

    Returns:
        numpy.ndarray: The normalized data of shape (N, D).
    """

    normalized_data = np.zeros_like(data)

    # ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ Assignment 4.1 ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰ #
    # TODO:                                                             #
    # Implement the function that normalizes the data to have zero mean #
    # and unit variance. The normalization is done over the first       #
    # dimension.                                                        #
    #                                                                   #
    # Good luck!                                                        #
    # ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰ #
    # 🌀 INCEPTION 🌀 (Your code begins its journey here. 🚀 Do not delete this line.)

    mean = torch.mean(data, axis=0)
    std = torch.std(data, axis=0)
    normalized_data = (data - mean) / std

    # 🌀 TERMINATION 🌀 (Your code reaches its end. 🏁 Do not delete this line.)

    return normalized_data