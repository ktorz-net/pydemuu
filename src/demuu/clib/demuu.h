/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 *   libDemuu
 *   A library dedicated to Decision Making under-uncertainty build on Bayesian-based Markov-models.
 * 
 * 
 *   STRUCTURE MODULE:
 *       - DuCode         : a fixed size array of digits (unsigned integers)
 *       - DuVector       : a fixed size array of values (doubles)
 *       - DuBench        : a dynamic-size collection of DuCode coupled to DuVector (i -> code and vector OR i -> digit and value)
 *       - DuTree         : a tree based DuCode (input code -> output digit )
 * 
 *   FUNCTION MODULE:
 *       - DuValueFct     : Determine a value from a code (in a given inputRanges)
 *       - DuFunction     : Determine a code+vector from a code
 *       <- BmDistbutor    : Determine a [code+vector distribution] from a code (used as Bayesian nodes) >
 * 
 *   COMPONENT MODULE:
 *       - DuCondition    : Represent conditional probabilities of a variable [input code -> digit distribution] (i.e. Bayesian Network's Node)
 *       - DuInferer      : Define a Bayesian Network as P(output | input) - potentially Dynamic P(state' | state) or P(state' | state, action)
 *       - DuEvaluator    : A value function over multiple criteria
 *
 *   MODEL MODUL:
 *       <- BmModel        : Define a Factored Markov Decision Process $<S, A, t, r>$ >
 *       <- BmQTable       : Define a QValues structure.
 * 
 *   SOLVER MODULE:
 *       <- BmSolver_valueIt : DuInferer (transition), DuEvaluator (cost/reward), DuFunction (policy/value)
 *       <-          : code (state) + code (action) -> value                    >
 * 
 * 
 *   LICENSE: MIT License
 *
 *   Copyright © 2022-2025 Guillaume Lozenguez.
 * 
 *   Permission is hereby granted, free of charge, to any person obtaining a
 *   copy of this software and associated documentation files (the "Software"),
 *   to deal in the Software without restriction, including without limitation
 *   the rights to use, copy, modify, merge, publish, distribute, sublicense,
 *   and/or sell copies of the Software, and to permit persons to whom the
 *   Software is furnished to do so, subject to the following conditions:
 *
 *   The above copyright notice and this permission notice shall be included in
 *   all copies or substantial portions of the software.
 *   
 *   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 *   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 *   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 *   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 *   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 *   IN THE SOFTWARE.
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

#ifndef DEMUU_H
#define DEMUU_H

#include <stdlib.h>


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   B A S I S                                                   *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

#ifndef digit
#define digit unsigned short
#endif

#ifndef hash
#define hash unsigned long long
#endif

#ifndef bool
typedef digit bool;
#define true 1
#define false 0
#endif

/* Clasical constructor/dextructor */
#define newEmpty(Type) malloc(sizeof(Type))
#define delEmpty(instance) free(instance)

/* Array manipulation */
#define newEmptyArray(Type, size) malloc( sizeof(Type)*(size+1) )
#define deleteEmptyArray(instance) free(instance)
#define array_on(instance, index) instance+(index-1)
#define array_at(instance, index) instance[index-1]
#define array_at_set(instance, index, value) instance[index-1]= value


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   S T R U C T U R E :  C O D E                                *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
    digit *dsc;
} DuCode;

//-- Constructor --
DuCode* newDuCode(digit dimension);
DuCode* newDuCode_numbers( digit dimension, digit* numbers );
DuCode* newDuCode_all(digit dimension, digit defaultValue);
DuCode* newDuCodeAs( DuCode* model );

DuCode* DuCode_create( DuCode* self, digit dimension );
DuCode* DuCode_create_numbers( DuCode* self, digit dimension, digit* numbers );
DuCode* DuCode_create_all( DuCode* self, digit dimension, digit defaultValue );
DuCode* DuCode_createAs( DuCode* self, DuCode* model );

DuCode* DuCode_createMerge( DuCode* self, digit numberOfCodes, DuCode ** codes );

//-- Destructor --
void deleteDuCode( DuCode* instance );
DuCode* DuCode_destroy( DuCode* self );

//-- Accessor --
digit DuCode_dimention( DuCode* self );
digit DuCode_digit( DuCode* self, digit index );
digit DuCode_count( DuCode* self, digit value );
hash DuCode_sum( DuCode* self );
hash DuCode_product( DuCode* self );

//-- Re-Initializer --
DuCode* DuCode_reinit( DuCode* self, digit newDimension );

DuCode* DuCode_copy( DuCode* self, DuCode* model);
DuCode* DuCode_copyNumbers( DuCode* self, DuCode* model);

//-- Construction --
DuCode* DuCode_redimention( DuCode* self, digit newDimension);
DuCode* DuCode_setAll( DuCode* self, digit value );
DuCode* DuCode_at_set( DuCode* self, digit index, digit value );
DuCode* DuCode_at_increment( DuCode* self, digit index, digit value );
DuCode* DuCode_at_decrement( DuCode* self, digit index, digit value );

DuCode* DuCode_setNumbers( DuCode* self, digit* numbers );

//-- Operator --
void DuCode_sort( DuCode* self );
void DuCode_switch( DuCode* self, DuCode* anotherCode );
digit DuCode_search( DuCode* self, digit value );

//-- Test --
bool DuCode_isEqualTo( DuCode* self, DuCode* another );
bool DuCode_isGreaterThan( DuCode* self, DuCode* another );
bool DuCode_isSmallerThan( DuCode* self, DuCode* another );

//-- As Configuration (a DuCode configuration varring in a space defined by a ranges DuCode 'self' ) --
hash DuCode_keyOf( DuCode* self, DuCode* code);       // get the key value of the code regarding given ranges ( i.e. 0 <= self.numbers[i] < ranges[i] )

DuCode* DuCode_setCode_onKey( DuCode* self, DuCode* configuration, hash key ); // set the code as a key value in given ranges
DuCode* DuCode_setCodeFirst( DuCode* self, DuCode* configuration ); // set the code as a key value in given ranges
DuCode* DuCode_setCodeLast( DuCode* self, DuCode* configuration ); // set the code as a key value in given ranges

DuCode* DuCode_newDuCodeOnKey( DuCode* self, hash key ); // set the code as a key value in given ranges
DuCode* DuCode_newDuCodeFirst( DuCode* self ); // set the code as a key value in given ranges
DuCode* DuCode_newDuCodeLast( DuCode* self ); // set the code as a key value in given ranges

DuCode* DuCode_nextCode( DuCode* self, DuCode* configuration ); // set the code as a key value in given ranges
DuCode* DuCode_previousCode( DuCode* self, DuCode* configuration ); // set the code as a key value in given ranges
bool DuCode_isIncluding( DuCode* self, DuCode* configuration ); // set the code as a key value in given ranges

//-- Mask --
DuCode* DuCode_newDuCodeMask(DuCode* self, DuCode* mask);

//-- Printing --
char* DuCode_print( DuCode* self, char* buffer);   // print `self` at the end of `output`


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   S T R U C T U R E :  V E C T O R                            *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  digit dimention;
  double * values;
} DuVector;

//-- Constructor --
DuVector* newDuVector( digit dimension );
DuVector* newDuVector_values( digit dimension, double* values );
DuVector* newDuVector_all( digit dimension, double value );
DuVector* newDuVectorAs( DuVector* model );

DuVector* DuVector_create( DuVector* self, digit dimension );
DuVector* DuVector_create_values( DuVector* self, digit dimension, double* values );
DuVector* DuVector_create_all( DuVector* self, digit dimension, double value );
DuVector* DuVector_createAs( DuVector* self, DuVector* model );

//-- Destructor --
DuVector* DuVector_destroy( DuVector* self );
void deleteDuVector( DuVector* self );

//-- Re-Initialize --
DuVector* DuVector_reinit( DuVector* self, digit newDimension );
DuVector* DuVector_copy( DuVector* self, DuVector* model );

//-- Accessor --
digit DuVector_dimention( DuVector* self );
double DuVector_value( DuVector* self, digit i );

//-- Construction --
DuVector* DuVector_redimention(DuVector* self, digit newDimension);
double DuVector_at_set( DuVector* self, digit i, double value );
DuVector* DuVector_setValues( DuVector* self, double* values );

//-- Operation --
double DuVector_sum( DuVector* self );
double DuVector_product( DuVector* self );

//-- Test --
bool DuVector_isEqualTo( DuVector* self, DuVector* another );
bool DuVector_isGreaterThan( DuVector* self, DuVector* another );
bool DuVector_isSmallerThan( DuVector* self, DuVector* another );

//-- Printing --
char* DuVector_print( DuVector* self, char* output );
char* DuVector_format_print( DuVector* self, char* format, char* buffer);


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   S T R U C T U R E :  B E N C H                              *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  digit capacity, start, size;
  digit codeDim, vectDim;
  DuCode   ** codes;
  DuVector ** vects;
} DuBench;

//-- Constructor --
DuBench* newDuBench( digit capacity );
DuBench* newDuBench_codeDim_vectorDim( digit capacity, digit codeDim, digit vectorDim );
DuBench* newDuBench_startDigit_value( digit capacity, digit aDigit, double value );
DuBench* newDuBench_startWithCode_vector( digit capacity, DuCode* newCode, DuVector* newVector );
DuBench* newDuBenchAs( DuBench* model );

DuBench* DuBench_create( DuBench* self, digit capacity );
DuBench* DuBench_create_codeDim_vectorDim( DuBench* self, digit capacity, digit codeDim, digit vectorDim );
DuBench* DuBench_createAs( DuBench* self, DuBench* model );

//-- Destructor --
DuBench* DuBench_destroy( DuBench* self);
void deleteDuBench( DuBench* self);

//-- Re-Initializer --
DuBench* DuBench_reinit( DuBench* self, digit capacity );

//-- Accessor --
digit DuBench_size( DuBench* self);

digit DuBench_codeDimention( DuBench* self);
digit DuBench_vectorDimention( DuBench* self);

DuCode* DuBench_codeAt( DuBench* self, digit i );
DuVector* DuBench_vectorAt( DuBench* self, digit i );

digit DuBench_digitAt( DuBench* self, digit i );
double DuBench_valueAt( DuBench* self, digit i );

digit DuBench_at_digit( DuBench* self, digit i, digit j );
double DuBench_at_value( DuBench* self, digit i, digit j );

//-- Construction --
//void DuBench_resizeCapacity_start( DuBench* self, digit newCapacity, digit start );
void DuBench_resizeCapacity( DuBench* self, digit newCapacity);
//void DuBench_resizeCapacityFront( DuBench* self, digit newCapacity);
digit DuBench_attachCode_vector( DuBench* self, DuCode* newCode, DuVector* newVector );
digit DuBench_attachFrontCode_vector( DuBench* self, DuCode* newCode, DuVector* newVector );

DuCode* DuBench_detach( DuBench* self );
DuCode* DuBench_detachFront( DuBench* self );
//DuCode* DuBench_detach( DuBench* self, digit i );

DuBench* DuBench_increase( DuBench* self, digit number );
DuBench* DuBench_increaseFront( DuBench* self, digit number );

digit DuBench_attachCode( DuBench* self, DuCode* newItem );
digit DuBench_attachVector( DuBench* self, DuVector* newItem );

void DuBench_switch( DuBench* self, DuBench* doppleganger);

//-- Construction Basic --
digit DuBench_addDigit_value( DuBench* self, digit d, double v );
DuBench* DuBench_at_setDigit( DuBench* self, digit i, digit aDigit );
DuBench* DuBench_at_setValue( DuBench* self, digit i, double value );

//void DuBench_add( DuBench *self, DuBench *another );
void DuBench_add_reducted( DuBench* self, DuBench* another, DuCode* mask );

//-- Operators --
typedef bool (*fctptr_DuBench_compare)(DuBench*,digit,digit);
digit DuBench_sort( DuBench* self, fctptr_DuBench_compare compare );
digit DuBench_switchAt_at( DuBench* self, digit id1, digit id2 );

//-- Comparison --

bool DuBench_is_codeGreater(DuBench* self, digit i1, digit i2);
bool DuBench_is_codeSmaller(DuBench* self, digit i1, digit i2);
bool DuBench_is_vectorGreater(DuBench* self, digit i1, digit i2);
bool DuBench_is_vectorSmaller(DuBench* self, digit i1, digit i2);

//-- Test --

//-- Printing --
char* DuBench_print( DuBench* self, char* output); // print `self` at the end of `output`
char* DuBench_printCodes(DuBench* self, char* output);
//char* DuBench_printVector(DuBench* self, char* output);
char* DuBench_printNetwork(DuBench* self, char* output);


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   S T R U C T U R E :  T R E E                                *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * Apply a tree structure to a Space for clustering states
 * in a finit number of options.
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  DuCode* inputRanges;
  digit capacity, size;
  digit** branches;    // -> digit* branchvariable AND Reductor** // Funnel** branchSelector AND digit** branches ?
} DuTree;

//-- Constructor --
DuTree* newDuTree( digit binarySpaceSize );
DuTree* newDuTreeWith( DuCode* newSpace );

DuTree* DuTree_createWhith( DuTree* self, DuCode* input );

//-- Destructor --
DuTree* DuTree_destroy( DuTree* self);
void deleteDuTree( DuTree* self );

//-- Re-Initializer --
DuTree* DuTree_reinitWith( DuTree* self, DuCode* newSpace );

DuTree* DuTree_clearWhith_on( DuTree* self, digit index, digit defaultOption );
DuTree* DuTree_clearOn( DuTree* self, digit defaultOption );

//-- Accessor --
digit DuTree_dimention( DuTree* self );
digit DuTree_size( DuTree* self );
DuCode* DuTree_inputRanges( DuTree* self );
digit DuTree_at( DuTree* self, DuCode* code ); // Return the option number of a code/state.

//-- output --
digit DuTreeChild( digit key );
digit DuTreeLeaf( digit key );

//-- Construction --
void DuTree_reziseCapacity( DuTree* self, digit newCapacity );
void DuTree_reziseCompleteCapacity( DuTree* self );

digit DuTree_at_set( DuTree* self, DuCode* code, digit output ); // set the ouput value of a code or a partial code (with 0), return the number of potential dead branches
digit DuTree_at_readOrder_set( DuTree* self, DuCode* code, DuCode* codeOrder, digit output );

//-- Branch Accessor --
digit DuTree_branchSize( DuTree* self, digit iBranch );
digit DuTree_branch_stateIndex( DuTree* self, digit iBranch, digit state );
digit DuTree_branch_state( DuTree* self, digit iBranch, digit state );
digit DuTree_branch_stateIsLeaf( DuTree* self, digit iBranch, digit state );
digit DuTree_branch_stateOption( DuTree* self, digit iBranch, digit state );
digit DuTree_branch_stateLeaf( DuTree* self, digit iBranch, digit state );
digit DuTree_branchVariable( DuTree* self, digit iBranch ); // Return the variable index represented by the branch.
digit DuTree_branchStart( DuTree* self, digit iBranch );
digit DuTree_branchBound( DuTree* self, digit iBranch );
digit DuTree_branchStep( DuTree* self, digit iBranch );
digit DuTree_branchNumberOfOutputs( DuTree* self, digit branch ); // Return the number of differents output
digit DuTree_deepOf( DuTree* self, DuCode* code); // Return the number of branch to cross before reaching the output.

//-- Branch Construction --
digit DuTree_newBranch( DuTree* self, digit iVariable, digit start, digit bound, digit step );
digit DuTree_newBranch_full( DuTree* self, digit iVariable, digit defaultOption);
digit DuTree_newBranch_binary_options( DuTree* self, digit iVariable, digit  afterValue, digit option1, digit option2);
digit DuTree_newBranch_pivot_options( DuTree* self, digit iVariable, digit onValue, digit optionBefore, digit optionOn, digit optionAfter);
void DuTree_branch_state_connect( DuTree* self, digit branchA, digit stateA, digit branchB );
void DuTree_branch_state_setOption( DuTree* self, digit branchA, digit iState, digit outbut );

//-- Cleanning --
digit DuTree_cleanDeadBranches( DuTree* self); // Detect and remove detached branches (or DuTree_update, DuTree_regenerate : rebuild the tree without dead branches)
digit DuTree_removeBranch( DuTree* self, digit iBranch); // Remove a branch: (must not change the order or the numerotation of the branch -> maintain a list of removed branches)

//-- Generating --
DuBench* DuTree_asNewBench( DuTree* self );
void DuTree_fromBench( DuTree* self, DuBench* model );

//-- Printing --
char* DuTree_branch_print( DuTree* self, digit iBranch, char* output );

char* DuTree_print( DuTree* self, char* output);
char* DuTree_print_sep( DuTree* self, char* output, char* separator );
char* DuTree_print( DuTree* self, char* output);

char* DuTree_printInside( DuTree* self, char* output); // print `self` at the end of `output`


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   F U N C T I O N  :  V A L U E F C T                         *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * code -> value
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  DuTree* selector;
  DuVector* outputs;
} DuValueFct;

//-- Constructor --
DuValueFct* newDuValueFctBasic( digit inputSize, digit outputSize );
DuValueFct* newDuValueFctWith( DuCode* newInputRanges, DuVector* newOutputs );

DuValueFct* DuValueFct_createWith( DuValueFct* self, DuCode* newInputRanges, DuVector* newOutputs );

//-- Destructor --
DuValueFct* DuValueFct_destroy( DuValueFct* self );
void deleteDuValueFct( DuValueFct* instance );

//-- Re-Initializer --
digit DuValueFct_reinitWith( DuValueFct* self, DuCode* newInputRanges, DuVector* newOutputs );

//-- Accessor --
DuTree* DuValueFct_selector( DuValueFct* self );
digit DuValueFct_inputDimention( DuValueFct* self );
digit DuValueFct_outputSize( DuValueFct* self );
DuCode* DuValueFct_inputRanges( DuValueFct* self );
DuVector* DuValueFct_outputs( DuValueFct* self );

double DuValueFct_from( DuValueFct* self, DuCode* input );

//-- Construction --
digit DuValueFct_addValue( DuValueFct* self, double ouputValue );
digit DuValueFct_ouputId_setValue( DuValueFct* self, digit ouputId, double ouputValue );
digit DuValueFct_from_set( DuValueFct* self, DuCode* input, digit ouputId );

//-- Instance tools --
void DuValueFct_switch(DuValueFct* self, DuValueFct* doppelganger);

//-- Generating --
DuBench* DuValueFct_asNewBench( DuValueFct* self );

//-- Printing --
char* DuValueFct_print(DuValueFct* self, char* buffer);
char* DuValueFct_printSep(DuValueFct* self, char* buffer, char* separator);


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   F U N C T I O N  :  F U N C T I O N                         *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * code -> code + vector
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  DuTree* selector;
  DuBench* outputs;
} DuFunction;

//-- Constructor --
DuFunction* newDuFunctionBasic( digit inputSize );
DuFunction* newDuFunctionWith( DuCode* newInputRanges, DuBench* newOutputs );

DuFunction* DuFunction_createWith( DuFunction* self, DuCode* newInputRanges, DuBench* newOutputs );

//-- Destructor --
DuFunction* DuFunction_destroy( DuFunction* self );
void deleteDuFunction( DuFunction* instance );

//-- Re-Initializer --
DuFunction* DuFunction_reinitWith( DuFunction* self, DuCode* newInputRanges, DuBench* newOutputs );
DuFunction* DuFunction_reinitWithDefault( DuFunction* self, DuCode* newInputRanges, DuCode* newDefaultOutput, double defaultValue );

//-- Accessor --
DuTree* DuFunction_selector( DuFunction* self );
digit DuFunction_inputDimention( DuFunction* self );
DuCode* DuFunction_inputRanges( DuFunction* self );
digit DuFunction_outputSize( DuFunction* self );
DuBench* DuFunction_outputs( DuFunction* self );

digit DuFunction_from( DuFunction* self, DuCode* input );
DuCode* DuFunction_codeFrom( DuFunction* self, DuCode* input );
double DuFunction_valueFrom( DuFunction* self, DuCode* input );

//-- Construction --
digit DuFunction_attachOuput( DuFunction* self, DuCode* newOuputCode, double ouputValue );
digit DuFunction_from_set( DuFunction* self, DuCode* input, digit ouputId );
// digit DuFunction_from_attach( DuFunction* self, DuCode* input, DuCode* newOutput, double value );

//-- Instance tools --
void DuFunction_switch(DuFunction* self, DuFunction* doppelganger);

//-- Printing --
char* DuFunction_print(DuFunction* self, char* output);
char* DuFunction_printSep(DuFunction* self, char* output, char* separator);

/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   F U N C T I O N  :  C O N D I T I O N                       *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * code -> bench
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  DuTree* selector;
  digit range;
  digit distribSize, distribCapacity;
  DuBench **distributions;
} DuCondition;

//-- Constructor --
DuCondition* newDuConditionBasic(digit domain);
DuCondition* newDuConditionWith(digit domain, DuCode* newInputRanges, DuBench* newDefaultDistrib);

DuCondition* DuCondition_createBasic(DuCondition* self, digit domain);
DuCondition* DuCondition_createWith(DuCondition* self, digit domain, DuCode* newInputRanges, DuBench* newDefaultDistrib);

//-- Destructor --
DuCondition* DuCondition_destroy(DuCondition* self);
void deleteDuCondition(DuCondition* instance);

//-- Re-Initializer --
digit DuCondition_reinitWith( DuCondition* self, digit domain, DuCode* newInputRanges, DuBench* newDistrib );
digit DuCondition_reinitDistributionsWith( DuCondition* self, DuBench* newDistrib );

//-- Accessor --
digit DuCondition_range( DuCondition* self );
DuTree* DuCondition_selector( DuCondition* self );
DuCode* DuCondition_parents( DuCondition* self );
DuBench* DuCondition_from( DuCondition* self, DuCode* configuration );
DuBench* DuCondition_fromKey( DuCondition* self, digit configKey );
digit DuCondition_distributionSize( DuCondition* self );
DuBench* DuCondition_distributionAt( DuCondition* self, digit iDistrib );

//-- Construction --
digit DuCondition_attach( DuCondition* self, DuBench* distribution );
digit DuCondition_from_attach( DuCondition* self, DuCode* configuration, DuBench* distribution );

//-- Instance tools --
void DuCondition_switch(DuCondition* self, DuCondition* doppelganger);

//-- Inferring --
DuBench* DuCondition_infer( DuCondition* self, DuBench* distribOverConfigurations );
DuBench* DuCondition_newDistributionByInfering( DuCondition* self, DuBench* distribOverConfigurations );
DuBench* DuCondition_newDistributionByInfering_mask( DuCondition* self, DuBench* longDistrib, DuCode* parentMask );

//-- Printing --
char* DuCondition_print(DuCondition* self, char* output);
char* DuCondition_printSep(DuCondition* self, char* output, char* separator);

char* DuCondition_printExtend(DuCondition* self, char* output); // print `self` at the end of `output`
char* DuCondition_printExtendSep(DuCondition* self, char* output, char* separator);

char* DuCondition_printIdentity( DuCondition* self, char* output ); // print `self` at the end of on `output`


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   F U N C T I O N  :  I N F E R E R                           *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * Define a Bayesian Network composed of state, action and tramsitional nodes
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  digit inputDimention, outputDimention, overallDimention;
  DuBench* network;
  DuCondition* nodes;
  DuBench* distribution;
} DuInferer;

//-- Constructor --
DuInferer* newDuInferer( DuCode* variableSpace, digit inputDimention, digit outputDimention );
DuInferer* newDuInfererStateAction( DuCode* stateSpace, DuCode* actionSpace );
DuInferer* newDuInfererStateActionShift( DuCode* stateSpace, DuCode* actionSpace, DuCode* shiftSpace );

DuInferer* DuInferer_create( DuInferer* self, DuCode* varDomains, digit inputDimention, digit outputDimention );

//-- Destructor --
DuInferer* DuInferer_destroy(DuInferer* self);
void deleteDuInferer(DuInferer* self);

//-- Accessor --
DuBench* DuInferer_distribution( DuInferer* self );

digit DuInferer_inputDimention( DuInferer* self );
digit DuInferer_outputDimention( DuInferer* self );
digit DuInferer_shiftDimention( DuInferer* self );
digit DuInferer_overallDimention( DuInferer* self );

DuCondition* DuInferer_node( DuInferer* self, digit iNode );
digit DuInferer_node_size( DuInferer* self, digit iVar );
DuCode* DuInferer_node_parents( DuInferer* self, digit iVar );

//-- Construction --
DuCondition* DuInferer_reinitIndependantNode( DuInferer* self, digit index );
DuCondition* DuInferer_node_reinitWith( DuInferer* self, digit index, DuCode* newParents );
DuCondition* DuInferer_node_reinitWith_withDefault( DuInferer* self, digit index, DuCode* newDependenceList, DuBench* newDefaultDistrib );

//-- Process --
DuBench* DuInferer_process( DuInferer* self, DuBench* inputDistribution );        // Return distribution over output varibales
DuBench* DuInferer_process_newOverallDistribution( DuInferer* self, DuBench* inputDistribution ); // Return distribution over all variables
DuBench* DuInferer_processState_Action( DuInferer* self, DuCode* state, DuCode* action ); // Return distribution over statePrime (output)

//-- Printing --
char* DuInferer_print(DuInferer* self, char* output); // print `self` at the end of `output`
char* DuInferer_printStateActionSignature(DuInferer* self, char* output); // print `self` at the end of `output`
char* DuInferer_printDependency(DuInferer* self, char* output); // print `self` at the end of `output`


/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   F U N C T I O N  :  E V A L U A T O R                       *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * Define a multi-critera Value function
 * (input -> value vector \times weight -> value)
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

typedef struct {
  DuCode* space;
  digit size;
  DuValueFct ** ccriteria;
  DuCode ** masks;
  DuVector* weights;
} DuEvaluator;

//-- Constructor --
DuEvaluator* newDuEvaluatorBasic( digit spaceDimention, digit numberOfCriteria );
DuEvaluator* newDuEvaluatorWith( DuCode* newSpace, digit numberOfCriteria );

DuEvaluator* DuEvaluator_createWith( DuEvaluator* self, DuCode* newSpace, digit numberOfCriteria );

//-- Destructor --
void deleteDuEvaluator( DuEvaluator* self );
DuEvaluator* DuEvaluator_destroy( DuEvaluator* self);

//-- Accessor --
DuCode* DuEvaluator_space( DuEvaluator* self );
digit DuEvaluator_numberOfCriteria( DuEvaluator* self );
DuValueFct* DuEvaluator_criterion( DuEvaluator* self, digit iCritirion );
DuVector* DuEvaluator_weights( DuEvaluator* self );
double DuEvaluator_criterion_weight( DuEvaluator* self, digit iCritirion );
DuCode* DuEvaluator_criterion_mask( DuEvaluator* self, digit iCritirion );

//-- Process --
double DuEvaluator_process( DuEvaluator* self, DuCode* input );
double DuEvaluator_criterion_process( DuEvaluator* self, digit iCriterion, DuCode* input );

double DuEvaluator_processState_action(DuEvaluator* self, DuCode* state, DuCode* action);
double DuEvaluator_processState_action_state(DuEvaluator* self, DuCode* state, DuCode* action, DuCode* statePrime);

//-- Construction --
DuEvaluator* DuEvaluator_reinitCriterion( DuEvaluator* self, digit numberOfCriterion );
DuValueFct* DuEvaluator_criterion_reinitWith( DuEvaluator* self, digit iCrit, DuCode* newDependenceMask, DuVector* newValues  );
void DuEvaluator_criterion_from_set( DuEvaluator* self, digit index, DuCode* option, digit output );
void DuEvaluator_criterion_setWeight( DuEvaluator* self, digit iCritirion, double weight );

//-- Infering --

//-- Printing --



/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   S O L V E R :  P O L I C Y                                  *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * Define Tree based Policy 
 * (state -> action + value)
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */

/* ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *   D e M U U   S O L V E R :  Q  V A L U E                                 *
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- *
 *
 * 
 * ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- */


#endif // DEMUU_H

