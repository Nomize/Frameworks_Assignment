import pandas as pd

# Define which columns to load
cols = ["title", "abstract", "publish_time", "journal", "authors"]

# Prepare an empty list to collect small pieces
chunks = []
chunk_size = 5000  # read 5k rows at a time
total_rows = 0
max_rows = 2000    # stop after 2000 rows

# Stream through the large file instead of loading all at once
for chunk in pd.read_csv("metadata.csv", usecols=cols, chunksize=chunk_size, low_memory=False):
    chunks.append(chunk)
    total_rows += len(chunk)
    if total_rows >= max_rows:
        break

# Concatenate only what we need (about 2000 rows)
sample_df = pd.concat(chunks).head(max_rows)

# Save to a small CSV file
sample_df.to_csv("metadata_sample.csv", index=False)

print("✅ Sample file created: metadata_sample.csv ({} rows)".format(len(sample_df)))
