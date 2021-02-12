https://stackoverflow.com/questions/52993123/firestore-security-rules-allow-user-to-create-doc-only-if-new-doc-id-is-same-as
user uid 체크
```js
service cloud.firestore {
  match /databases/{database}/documents {
  
    // Allow users to create a document for themselves in the users collection
    match /users/{document=**} {
      allow create: if request.resource.id == request.auth.uid &&
        !("admin" in request.resource.data);
    }
    
    // Allow users to read, write, update documents that have the same ID as their user id
    match /users/{userId} {   
        // Allow users to read their own profile (doc id same as user id)
      allow read: if request.auth.uid == userId;
      
      // Allow users to write / update their own profile as long as no "admin"
      // field is trying to be added or created - unless they are already an admin
      allow write, update: if request.auth.uid == userId &&
        (
          !("admin" in request.resource.data) ||
          get(/databases/$(database)/documents/users/$(request.auth.uid)).data.admin == true // allow admin to update their own profile
        )

      // Allow users to read their own feeds
      match /feeds/{document=**} {
        allow read: if request.auth.uid == userId;
      } 
    }
  }
}
```
