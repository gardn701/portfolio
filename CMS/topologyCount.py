
#
# We want to find how many unique wagon boards we need to construct.
#   Wagon boards have a certain number of T and D channels leaving each wagon.
#   They depend on the type of module and whether they are inner (closer to the beamline) or outer (further)
def main( inputFilePath , ignoreTriangleModules , beConservative , allowOverloadedParents ) :
    
    #LD persisted variables
    overloadedTopsLD = { } #tops that can happen with some redirecting of channls, only includes one side
    impossibleTopsLD = { } #tops that can't happen with current engine board, includes both inner and outer sides
    uniqueTopologyLD = { }
    topologyCountsLD = { }
    numEnginesLD     = 0
    # HD persisted variables
    uniqueTopologyHD = { }
    topologyCountsHD = { }
    impossibleTopsHD = { }
    numEnginesHD     = 0
    with open( inputFilePath ) as f:
    
        for engineLine in f.readlines() :
            # different fields separated by vertial bar '|'
            lineSplit = engineLine.strip().split( '|' )
    
            # fields lifted from file - hardcoded
            [ endCap , layer , cassette , mbIndex , MBType , organisation , approxPos ] = lineSplit[1].split( ',' )
            innerWagon  = lineSplit[2]
            outerWagon  = lineSplit[3]
    
            # topology list of lists of lists
            #   topology[ i'th module ][ DorT ] = number of D/T channels coming from the i'th wagon
            #       i'th module = ranges from 0 (closest to engine) to 2 (furthest), may not have all 3 entries
            #       DorT = 0 (D) or 1 (T)
            innerWagonTop = mapWagon( innerWagon , ignoreTriangleModules )
            outerWagonTop = mapWagon( outerWagon , ignoreTriangleModules )
    
            # attach engine information to beginning
            innerWagonTop.insert( 0 , organisation + 'I' )
            outerWagonTop.insert( 0 , organisation + 'O' )

            # count D and T channels
            #   check that they are less than requirements
            innerCounts = countDT( innerWagonTop )
            outerCounts = countDT( outerWagonTop )
            
            # make a key for these wagon topologies
            innerTopKey = makeWagonTopKey( innerWagonTop ) 
            outerTopKey = makeWagonTopKey( outerWagonTop )

            # check that we are only counting low density (LD.1) detector areas
            if 'LD' in MBType: 
    
                if len(innerWagonTop) > 4 or len(outerWagonTop) > 4 :
                    print 'More than 3 modules! What?!?!?!'
                    print 'Line from file:'
                    print engineLine

                # Each LD engine can handle 7 trigger (T) channels and 3 DAQ (D) channels on
                #  both the inner (I) and outer (O) sides. We are able to connect some
                #  channels from the opposite side so the absolute maximum is set by the
                #  the sum.
                numEnginesLD += 1
                if innerCounts[0]+outerCounts[0] > 6 or innerCounts[1]+outerCounts[1] > 14 :
                    engineTopKey = innerTopKey.join(outerTopKey)
                    if engineTopKey in impossibleTopsLD :
                        impossibleTopsLD[ engineTopKey ][2] += 1
                    else :
                        impossibleTopsLD[ engineTopKey ] = [ innerTopKey , outerTopKey , 1 ]
                else :
                    if innerCounts[0] > 3 or innerCounts[1] > 7:
                        if innerTopKey in overloadedTopsLD :
                            overloadedTopsLD[innerTopKey] += 1
                        else :
                            overloadedTopsLD[innerTopKey] =  1
                        #check if already found overloaded
                    #check if overloaded
                    if outerCounts[0] > 3 or outerCounts[1] > 7:
                        if outerTopKey in overloadedTopsLD :
                            overloadedTopsLD[outerTopKey] += 1
                        else :
                            overloadedTopsLD[outerTopKey] =  1
                        #check if already found overloaded
                    #check if overloaded
                #check for impossible
        
                # put the wagon topologies into the maps
                if innerTopKey not in topologyCountsLD :
                    uniqueTopologyLD[ innerTopKey ] = innerWagonTop
                    topologyCountsLD[ innerTopKey ] = 1
                else :
                    topologyCountsLD[ innerTopKey ] += 1
        
                if outerTopKey not in topologyCountsLD :
                    uniqueTopologyLD[ outerTopKey ] = outerWagonTop
                    topologyCountsLD[ outerTopKey ] = 1
                else :
                    topologyCountsLD[ outerTopKey ] += 1

            elif 'HD' in MBType:
                # Each HD engine can handle 42 T channels and 14 D channels
                #  HD engines only have one (inner) wagon ==> ignore outer wagon stuff
                numEnginesHD += 1
                if innerCounts[0] > 14 or innerCounts[1] > 42 :
                    # add to impossible types
                    if innerTopKey in impossibleTopsHD :
                        impossibleTopsHD[innerTopKey] += 1
                    else :
                        impossibleTopsHD[innerTopKey] = 1
                #check if impossible

                # put the wagon topologies into the maps
                if innerTopKey not in topologyCountsHD :
                    uniqueTopologyHD[ innerTopKey ] = innerWagonTop
                    topologyCountsHD[ innerTopKey ] = 1
                else :
                    topologyCountsHD[ innerTopKey ] += 1
        
            else :
                print 'Unknown MB type! %s' % ( engineLine )

        #end loop over engine lines
    
    #end open input file

    parentMapLD = createParentMap( uniqueTopologyLD , overloadedTopsLD , impossibleTopsLD , allowOverloadedParents , beConservative )
    parentMapHD = createParentMap( uniqueTopologyHD , [ ] , impossibleTopsHD , allowOverloadedParents , beConservative )

    # uniqueTopologies contains a map from keys to topologies
    # topologyCounts contains a map from keys to the number of each of these unique topologies
    # parentMap contains a map from keys to a list of subset keys
    
    print '=========================================================='

    legend( inputFilePath , beConservative , allowOverloadedParents , ignoreTriangleModules )

    print '=========================================================='
    print '=                          LD                            ='
    print '=========================================================='

    printParentMap( parentMapLD , topologyCountsLD , uniqueTopologyLD )

    print 'Num Overloaded Topologies: %d' % ( len(overloadedTopsLD) )
    print '   %8s | %5s' % ( 'Topology' , 'Count' )
    total = printTopologies( overloadedTopsLD.keys() , overloadedTopsLD , uniqueTopologyLD )
    print '    Total Count: %d' % ( total )

    print '----------------------------------------------------------'

    print 'Num Impossible Topologies: %d' % ( len(impossibleTopsLD) )
    print '      Inner | Outer    | Count'
    total = 0
    for engineKey in impossibleTopsLD :
        print '   %s | %s | %d' % ( 
                printWagon(uniqueTopologyLD[impossibleTopsLD[engineKey][0]]) ,
                printWagon(uniqueTopologyLD[impossibleTopsLD[engineKey][1]]) ,
                impossibleTopsLD[engineKey][2] )
        total += impossibleTopsLD[engineKey][2]
    print '         Total Count: %d' % ( total )

    print '----------------------------------------------------------'
    print ' Totals'
    print '   Engines        : %5d' % ( numEnginesLD )
    print '   Wagons         : %5d' % ( sum(topologyCountsLD.values()) )
    print '   Unique Wagons  : %5d' % ( len(uniqueTopologyLD) )
    print '   Needed Designs : %5d' % ( len(parentMapLD) )

    print '=========================================================='
    print '=                          HD                            ='
    print '=========================================================='

    printParentMap( parentMapHD , topologyCountsHD , uniqueTopologyHD )

    print 'Num Impossible Topologies: %d' % ( len(impossibleTopsHD) )
    print '      Topology | Count'
    total = printTopologies( impossibleTopsHD.keys() , impossibleTopsHD , uniqueTopologyHD )
    print '         Total Count: %d' % ( total )

    print '----------------------------------------------------------'
    print ' Totals'
    print '   Engines        : %5d' % ( numEnginesHD )
    print '   Wagons         : %5d' % ( sum(topologyCountsHD.values()) )
    print '   Unique Wagons  : %5d' % ( len(uniqueTopologyHD) )
    print '   Needed Designs : %5d' % ( len(parentMapHD) )

    print '=========================================================='
    return
#end main

################################################################
# Create a map from parents to list of subset topologies
def createParentMap( uniqueTopology , overloadedTops , impossibleTops , allowOverloadedParents , beConservative ) :

    import re

    # now we can loop over unique topologies and check if any of them
    #   are subsets of each other
    childMap = { }
    for topKey in uniqueTopology :
        for possParKey in uniqueTopology :
            #skip poss parent if it is apart of an impossible topology
            if possParKey in impossibleTops or possParKey in flatten(impossibleTops.values()) :
                continue
            #skip poss parent if it is an overloaded topology and overloaded parents are not allowed
            if not allowOverloadedParents and possParKey in overloadedTops :
                continue
            #skip if already pointing here
            if possParKey in childMap and childMap[possParKey] == topKey :
                continue
            #check if topKey is contained by possible parent
            if topKey != possParKey and isContainedBy( uniqueTopology[possParKey] , uniqueTopology[topKey] , beConservative ) :
                childMap[ topKey ] = possParKey
                break
            #end check for parent
        #end loop over possible parents
    #end loop over topologies
    #loop over childMap again, checking that everyone is pointed to root parent
    for topKey in childMap :
        maxParKey = topKey
        while maxParKey in childMap :
            maxParKey = childMap[maxParKey]
        #end while loop
        #reset to root parent
        childMap[topKey] = maxParKey
    #done loop over parent Map

    #invert parent map so that each absolute parent points to list of subsets
    parentMap = { }
    for childKey in childMap :
        parentKey = childMap[childKey]
        if parentKey in parentMap :
            parentMap[ parentKey ].append( childKey )
        else :
            parentMap[ parentKey ] = [ childKey ]
        #check if parentKey already in printingMap
    #end loop over children map

    # add topologies that are not in parent->child tree (isolated)
    for topKey in uniqueTopology :
        if topKey not in parentMap and topKey not in childMap :
            parentMap[topKey] = [ ]
    #end loop over top keys
    
    return parentMap

####################################################################
# Split input wagon string and count D channels and T channels
def mapWagon( readInWagonString , ignoreTriangleModules ) :

    cleanedWagonString = readInWagonString.strip('I \t[]O:') #remove prefix and suffix chars

    modules = []
    if not cleanedWagonString :
        return modules

    moduleStrings = cleanedWagonString.split( ';' ) # split cleaned wagon string into modules

    for moduleString in moduleStrings :
        # D and T channel lists are inside curly brackets and separated by white space
        
        # split up module string into global ID and channel listing
        moduleStringSplit = moduleString.split( '{' )
        moduleGlobalID = moduleStringSplit[0].strip( '() ->' )
        moduleType = moduleGlobalID.split( '.' )[0]

        #check if we should ignore triangles and then
        # check if module ID labels it as a triangle
        if ignoreTriangleModules and moduleType == 'cO' :
            continue

        channelStringList = ''
        if len(moduleStringSplit) > 1 :
            channelStringList = moduleStringSplit[1].strip( '}' )

        # split up channel string list into D and T channels
        #   D channels are listed first
        StrLists = channelStringList.split( 'T' , 1 )
        DStrList = ''
        TStrList = ''
        if len(StrLists) == 2 :
            DStrList = StrLists[0]
            TStrList = StrLists[1]
        elif len(StrLists) == 1 :
            DStrList = StrLists[0]
        else :
            print 'What is this line? %s' %( StrLists )

        # split str list into id list by stripping wrapping brackets
        #   and splitting on comma separators
        # filter removes non empty strings
        Dchannels = filter( None , DStrList.strip( 'D:() \t' ).split( ',' ))
        Tchannels = filter( None , TStrList.strip( 'T:() \t' ).split( ',' ))

        # count number of entries
        modules.append( [ moduleType , len(Dchannels) , len(Tchannels) ] )
    #end loop over module strings

    return modules 

####################################################################
# Count number of D and T channels in wagon topology
def countDT( wagonTopology ) :
    Dcount = 0
    Tcount = 0
    for mT,nD,nT in wagonTopology[1:] :
        Dcount += nD
        Tcount += nT
    #end loop over modules

    return [ Dcount , Tcount ]

####################################################################
# Recursively flatten a list to one list
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])

#####################################################################
# Make a key from the wagon topology input
#   The order of the number of D and T channels uniquely defines a wagon topology
def makeWagonTopKey( wagonTop ) :
    return ''.join( map( str , flatten( wagonTop ) ) )

#####################################################################
# Check if the input wagon topology is contained by the possible parent
# return true if wagonTopology IS a subset of possibleParent
def isContainedBy( possibleParent , wagonTopology , beConservative ) :
    
    if len(possibleParent) == len(wagonTopology) and possibleParent[0] == wagonTopology[0] :
        numExactlyEqual = 0
        for iModule in range(1,len(wagonTopology)) :
            if wagonTopology[iModule][1] > possibleParent[iModule][1] or wagonTopology[iModule][2] > possibleParent[iModule][2] :
                 #module channel members larger than possible parent => parent can't be a superset
                 return False
            #end check if module is not child of parent
            if beConservative and wagonTopology[iModule][0][0] != possibleParent[iModule][0][0]:
                return False
            #end conservative check on module types (first letter)
            if wagonTopology[iModule][1] == possibleParent[iModule][1] and wagonTopology[iModule][2] == possibleParent[iModule][2] :
                numExactlyEqual += 1
            #end check if channel count exactly equal
        #end loop over modules

        if numExactlyEqual >= len(wagonTopology)-1 :
            #channels are the same, so only difference could be channel type
            # if not caring about channel type, then these should NOT be parent/child related
            return False

        #made it through loop without exiting
        #   ==> all modules have less than or equal number of connections than possibleParent
        return True
    #check same number of modules in wagon

    #not same number of wagons
    return False

####################################################################
# Print a legend for reading the wagon topologies
def legend( inputFilePath , beConservative , allowOverloadedParents , ignoreTriangleModules ) :

    print 'Legend: D = DAQ channels and T = Trigger channels'
    print ' One Module = (type,nD,nT)'
    print ' Modules listed in radial order (beamline is to the left).'
    print ' Linear Type:'
    print '   towards  <- LI(FM,1,2)(FM,1,3)... | LO(FM,1,3)(FM,2,4)...'
    print '   beamline                          ^engine' 
    print ' Wedge Type:'
    print '   towards  <- | WO(FM,1,2)(FM,1,3)... <- outer'
    print '   beamline    | WI(FM,1,2)(FM,1,3)... <- inner'
    print '               ^engine'
    print 'Impossible = total D or total T is greater than engine can accept'
    print 'Overloaded = (D or T greater than number of channels on its side) and not Impossible'
    print '----------------------------------------------------------'
    print 'Ran with: %s' % ( inputFilePath )
    if beConservative :
        print 'Required module types to be the same for parents.'
    if allowOverloadedParents :
        print 'Allowed parent topologies to overload engine.'
    if ignoreTriangleModules :
        print 'Ignored triangle modules (cO).'

    return

###################################################################
# Print a wagon topolgy
#   return a string to be printed
def printWagon( wagonTop ) :
    wagonString = wagonTop[0]
    for moduleType,nD,nT in wagonTop[1:] :
        wagonString += '(%s,%d,%d)' % ( moduleType , nD , nT )
    #end loop over wagons
    return wagonString

##################################################################
# Print topologies passed through list of keys
#   Returns total
def printTopologies( keyList , topologyCounts , uniqueTopologies ) :
    total = 0
    for topKey in keyList :
        print '   %s | %5d' % ( printWagon(uniqueTopologies[topKey]) , topologyCounts[topKey] )
        total += topologyCounts[topKey]
    #end loop over children
    return total

###################################################################
# Print a topology map
def printParentMap( printingMap , topologyCounts , uniqueTopologies ) :
    # iterate through printing map to print
    for parentKey in printingMap :
        print '----------------------------------------------------------'
        #print parent
        print '   %s | %5s' % ( 'Topology' , 'Count' )
        print '   %s | %5d Parent' % ( printWagon(uniqueTopologies[parentKey]) , topologyCounts[parentKey] )
        #print children and get total
        total = topologyCounts[parentKey] + printTopologies( printingMap[parentKey] , topologyCounts , uniqueTopologies ) 
        print '    Total Count: %d' % ( total )
    #no more topologies to print
    print '----------------------------------------------------------'
    return

import argparse

if __name__ == '__main__' :

    # Do command line parsing
    parser = argparse.ArgumentParser(description='Count necessary wagon designs given a HG-CAL design text file')
    parser.add_argument( 'inputFilePath' , type=str, help='path to design text file to process')
    parser.add_argument( '--ignoreTriangleModules' , action='store_true' , default=False
            , help='Should we ignore triangle (cO) modules?')
    parser.add_argument( '--beConservative' , action='store_true' , default=False
            , help='Should we take the module type into account when deciding on inheritance?')
    parser.add_argument( '--allowOverloadedParents' , action='store_true' , default=False 
            , help='Should we allow topologies that overload the engine be accepted as a parent?' )

    args = parser.parse_args()

    # Pass variables to main
    main( args.inputFilePath , args.ignoreTriangleModules , args.beConservative , args.allowOverloadedParents )

