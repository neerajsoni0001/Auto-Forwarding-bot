from env import CONNECTION_STRING
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(CONNECTION_STRING)
mydatabase = client['mydatabase']
collection = mydatabase['collection']

def get_all_sources():
    try:
        # Fetch all documents from the collection
        documents = list(collection.find())

        # Extract "sources" arrays from each document
        sources = []
        for doc in documents:
            if "sources" in doc and isinstance(doc["sources"], list):
                sources.extend(doc["sources"])  # Combine all sources arrays

        return sources
    except Exception as e:
        return f"Error Occurred: {e}"
    

def get_all_destinations():
    try:
        # Fetch all documents from the collection
        documents = list(collection.find())

        # Extract "destinations" arrays from each document
        destinations = []
        for doc in documents:
            if "destinations" in doc and isinstance(doc["destinations"], list):
                destinations.extend(doc["destinations"])

        return destinations
    except Exception as e:
        return f"Error Occurred: {e}"

def add_source(new_source):
    """
    Adds a new source to the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        new_source: The source to add to the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Add the new source to the 'sources' array using $addToSet (avoids duplicates)
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},  # Specify the document to update
            {"$addToSet": {"sources": new_source}}
        )

        if result.modified_count > 0:
            return f"Successfully added source '{new_source}'"
        else:
            return f"No changes made. Either the document doesn't exist or the source is already in the array."
    except Exception as e:
        return f"Error Occurred: {e}"

def remove_source(document_id, source_to_remove):
    """
    Removes a source from the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        source_to_remove: The source to remove from the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Remove the source from the 'sources' array using $pull
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},
            {"$pull": {"sources": source_to_remove}}
        )

        if result.modified_count > 0:
            return f"Successfully removed source '{source_to_remove}' from document {document_id}."
        else:
            return f"No changes made. Either the document doesn't exist or the source wasn't in the array."
    except Exception as e:
        return f"Error Occurred: {e}"
    
def add_destination(new_destination):
    """
    Adds a new source to the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        new_source: The source to add to the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Add the new source to the 'sources' array using $addToSet (avoids duplicates)
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},
            {"$addToSet": {"destinations": new_destination}}
        )

        if result.modified_count > 0:
            return f"Successfully added source '{new_destination}'"
        else:
            return f"No changes made. Either the document doesn't exist or the source is already in the array."
    except Exception as e:
        return f"Error Occurred: {e}"


def remove_destination(document_id, destination_to_remove):
    """
    Removes a source from the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        source_to_remove: The source to remove from the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Remove the source from the 'sources' array using $pull
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},
            {"$pull": {"destinations": destination_to_remove}}
        )

        if result.modified_count > 0:
            return f"Successfully removed source '{destination_to_remove}' from document {document_id}."
        else:
            return f"No changes made. Either the document doesn't exist or the source wasn't in the array."
    except Exception as e:
        return f"Error Occurred: {e}"

def update_status(new_status):
    """
    Updates the 'status' field of a document.

    Args:
        new_status: The new value to set for the 'status' field.

    Returns:
        str: Success message or error message.
    """
    try:
        # Update the 'status' field for the first document that matches the query
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},  # Specify the document to update
            {"$set": {"status": new_status}}  # Update the 'status' field
        )

        if result.modified_count > 0:
            return f"Successfully updated status to '{new_status}'"
        else:
            return f"No changes made. Either the document doesn't exist or the status is already '{new_status}'."
    except Exception as e:
        return f"Error Occurred: {e}"

def image_status(new_status):
    try:
        # Update the 'status' field for the first document that matches the query
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},  # Specify the document to update
            {"$set": {"photo_status": new_status}}  # Update the 'status' field
        )

        if result.modified_count > 0:
            return f"Successfully updated photo status to '{new_status}'"
        else:
            return f"No changes made. Either the document doesn't exist or the status is already '{new_status}'."
    except Exception as e:
        return f"Error Occurred: {e}"
    
def get_input_usernames():
    try:
        # Fetch all documents from the collection
        documents = list(collection.find())

        # Extract "destinations" arrays from each document
        input_usernames = []
        for doc in documents:
            if "input_usernames" in doc and isinstance(doc["input_usernames"], list):
                input_usernames.extend(doc["input_usernames"])

        return input_usernames
    except Exception as e:
        return f"Error Occurred: {e}"
    
def get_output_usernames():
    try:
        # Fetch all documents from the collection
        documents = list(collection.find())

        # Extract "destinations" arrays from each document
        output_usernames = []
        for doc in documents:
            if "output_usernames" in doc and isinstance(doc["output_usernames"], list):
                output_usernames.extend(doc["input_usernames"])

        return output_usernames
    except Exception as e:
        return f"Error Occurred: {e}"
    

def add_input_username(new_username):
    """
    Adds a new source to the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        new_source: The source to add to the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Add the new source to the 'sources' array using $addToSet (avoids duplicates)
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},  # Specify the document to update
            {"$addToSet": {"input_usernames": new_username}}
        )

        if result.modified_count > 0:
            return f"Successfully added Username '{new_username}'"
        else:
            return f"No changes made. Either the document doesn't exist or the source is already in the array."
    except Exception as e:
        return f"Error Occurred: {e}"

def remove_input_username(username_to_remove):
    """
    Removes a source from the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        source_to_remove: The source to remove from the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Remove the source from the 'sources' array using $pull
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},
            {"$pull": {"input_usernames": username_to_remove}}
        )

        if result.modified_count > 0:
            return f"Successfully removed source '{username_to_remove}' from document."
        else:
            return f"No changes made. Either the document doesn't exist or the source wasn't in the array."
    except Exception as e:
        return f"Error Occurred: {e}"
    

def add_output_username(new_username):
    """
    Adds a new source to the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        new_source: The source to add to the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Add the new source to the 'sources' array using $addToSet (avoids duplicates)
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},  # Specify the document to update
            {"$addToSet": {"output_usernames": new_username}}
        )

        if result.modified_count > 0:
            return f"Successfully added Username '{new_username}'"
        else:
            return f"No changes made. Either the document doesn't exist or the source is already in the array."
    except Exception as e:
        return f"Error Occurred: {e}"

def remove_output_username(username_to_remove):
    """
    Removes a source from the 'sources' array of a document.

    Args:
        document_id: The ID of the document to update.
        source_to_remove: The source to remove from the 'sources' array.

    Returns:
        str: Success message or error message.
    """
    try:
        # Remove the source from the 'sources' array using $pull
        result = collection.update_one(
            {"_id": ObjectId("6783cc43d9fed44719153b4d")},
            {"$pull": {"output_usernames": username_to_remove}}
        )

        if result.modified_count > 0:
            return f"Successfully removed source '{username_to_remove}' from document."
        else:
            return f"No changes made. Either the document doesn't exist or the source wasn't in the array."
    except Exception as e:
        return f"Error Occurred: {e}"
    

def get_image_status():
    try:
        result = collection.find_one({"_id": ObjectId("6783cc43d9fed44719153b4d")})
        return result.get("photo_status")
    except Exception as e:
        return f"Error Occurred: {e}"
    
def get_banned_url():
    try:
        result = collection.find_one({
            "_id": ObjectId("6783cc43d9fed44719153b4d")
        })

        return result.get("banned_urls")
    except Exception as e:
        return f"Error Occurred: {e}"
    
def get_output_url():
    try:
        result = collection.find_one({
            "_id": ObjectId("6783cc43d9fed44719153b4d")
        })

        return result.get("output_url")
        
    except Exception as e:
        return f"Error Occurred: {e}"
    
def insert_banned_url(url):
    try:
        result = collection.update_one({
            "_id": ObjectId("6783cc43d9fed44719153b4d")
        }, {
            "$addToSet": {
                "banned_urls": url
            }
        })

        if result.modified_count >= 1:
            return "Banned Url upddated successfully"
        else:
            return "Something went wrong while adding Banned Url"

    except Exception as e:
        return f"Error Occurred: {e}"
    
def update_output_url(url):
    try:
        result = collection.update_one({
            "_id": ObjectId("6783cc43d9fed44719153b4d")
        }, {
            "$set": {
                "output_url": url
            }
        })

        if result.modified_count >= 1:
            return "Output Url upddated successfully"
        else:
            return "Something went wrong while adding Output Url"

    except Exception as e:
        return f"Error Occurred: {e}"
    
def insert_input_usernames(input_username):
    try:
        result = collection.update_one({
                "_id": ObjectId("6783cc43d9fed44719153b4d")}, 
                {
                "$addToSet": {
                    "input_usernames": input_username
                }})

        if result.modified_count >=1:
            return f"Added username to Banned List"
        else:
            return f"Something went wrong!"
    except Exception as e:
        return f"Error Occurred: {e}"
    
def remove_input_username(input_username):
    try:
        result = collection.update_one({
            "_id": ObjectId("6783cc43d9fed44719153b4d")
        }, {
            "$pull": {
                "input_usernames": input_username
            }
        })

        if result.modified_count >= 1:
            return f"Removed username from Banned List"
        else:
            return f"Something went wrong!"
    except Exception as e:
        return f"Error Occurred: {e}"

def update_output_username(output_username):
    try:
        result = collection.update_one({
            "_id": ObjectId("6783cc43d9fed44719153b4d")
        }, {
            "$set": {
                "output_username": output_username
            }
        })

        if result.modified_count >= 1:
            return f"Output username updated successfully!"
        
        else:
            return "Something went wrong"
        
    except Exception as e:
        return f"Error Occurred: {e}"
    
def get_output_username():
    try:
        result = collection.find_one({
            "_id": ObjectId("6783cc43d9fed44719153b4d")
        })

        if result:
            return result.get("output_username")  # Use .get() on the document (dictionary)
        else:
            return "No document found with the specified ID."
    except Exception as e:
        return f"Error Occurred: {e}"
