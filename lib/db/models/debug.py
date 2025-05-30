from lib.models.author import Author
from lib.models.magazine import Magazine

# Example usage
author = Author("John Doe")
author.save()

mag = Magazine("Tech World", "Technology")
mag.save()

article = author.add_article(mag, "The Rise of AI")

print(author.articles())
print(author.magazines())
print(mag.article_titles())
print(mag.contributors())
print(author.topic_areas())