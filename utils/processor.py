import re


def clean_text(text):

    text = text.replace("\r", "")

    text = re.sub(r"[ \t]+", " ", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def chunk_text(text, max_chunk_size=1200):

    # Split by page markers
    pages = re.split(r"========== PAGE (\d+) ==========", text)

    chunks = []

    # pages format:
    # ["", "1", page1_text, "2", page2_text, ...]

    for i in range(1, len(pages), 2):

        page_number = int(pages[i])

        page_text = pages[i + 1].strip()

        # Skip completely empty pages
        if not page_text:
            continue

        paragraphs = page_text.split("\n\n")

        current_chunk = ""

        title = ""

        for para in paragraphs:

            para = para.strip()

            # Skip empty paragraphs
            if not para:
                continue

            # First meaningful paragraph becomes title
            if title == "":
                title = para.split("\n")[0]

            # If paragraph fits, keep adding
            if len(current_chunk) + len(para) <= max_chunk_size:

                current_chunk += para + "\n\n"

            else:

                # Save previous chunk only if it has text
                if current_chunk.strip():

                    chunks.append({

                        "page": page_number,

                        "title": title,

                        "text": current_chunk.strip()

                    })

                # Start new chunk
                current_chunk = para + "\n\n"

                # Update title for new chunk
                title = para.split("\n")[0]

        # Save last chunk
        if current_chunk.strip():

            chunks.append({

                "page": page_number,

                "title": title,

                "text": current_chunk.strip()

            })

    return chunks