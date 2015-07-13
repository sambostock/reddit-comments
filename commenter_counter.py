#!/usr/bin/env python
import praw
import sys

user_agent = 'Unique Commenter Counter 0.1 by /u/bosticko'
r = praw.Reddit(user_agent=user_agent)

# Get the submission id from the user or arguments
if len(sys.argv) > 1:
    # Use id from args
    submission_id = sys.argv[1]
else:
    # Get id from command line
    print "Enter the submission id:"
    submission_id = raw_input().rstrip()

submission = r.get_submission(submission_id=submission_id)
submission.replace_more_comments(limit=None, threshold=0)
flat_comments = praw.helpers.flatten_tree(submission.comments)

authors = set(map(lambda c: c.author.name, flat_comments))

print str(len(submission.comments)) + " top level comments"
print str(len(flat_comments)) + " total comments"
print str(len(authors)) + " unique commenters"
