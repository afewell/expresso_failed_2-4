def parse_block(block_data: str) -> dict:
    """Parse block data into a dictionary

    Args:
    block_data: string of the block data

    Returns:
    Dictionary representation of the block data
    """
    block_list = block_data.strip().split("\n")
    block_dict = {}

    # Extract block header information
    block_dict["index"] = int(block_list[0].split(":")[1])
    block_dict["timestamp"] = int(block_list[1].split(":")[1])
    block_dict["data"] = block_list[2].split(":")[1]
    block_dict["previous_hash"] = block_list[3].split(":")[1]
    block_dict["hash"] = block_list[4].split(":")[1]

    return block_dict