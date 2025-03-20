#start

    #create an empty dictionary to store course information
        #initialize courses as an empty dictionary

    #input course ID and course name pairs from the user
        #repeat
        #display "Enter course ID (or type 'STOP' to finish):"
        #input courseID
        #if courseID is "STOP" THEN
            #Exit input loop


    #Display "Enter course name for " + courseID + ":"
        #Input courseName

    #Add courseID and courseName to courses dictionary UNTIL courseID is "STOP"

    #Ask the user for a subject
        #Display "Enter a subject to search for (e.g., COS):"
        #Input subject

    #display courses that match the subject
        #initialize found as false
        #for each courseID in courses
            #if courseID starts with subject THEN
                #Display courseID + ": " + courses[courseID]
                #Set found as True
            #endif end for loop

    #if no matching courses are found
         #if found is false then
            #display "No courses found for subject: " + subject
            #end if statement

#end