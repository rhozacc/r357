// This JavaScript will create conditional dropdown menus for gsheets.
// Place in the Script editor, change code.



function onEdit() {  // Runs automatically when the user edits the sheet

  var ss = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var e = ss.getActiveCell();
  var col = e.getColumn();     // Get the col and row num of the edited cell
  var row = e.getRow();
  var datass = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("importer");    // Get the sheet and table with the list of dropdowns
  
  
  if(row == 1 && col > 5){ // Make sure that the edited cell is part of the table
    
    e.offset(1, 0).clearContent().clearDataValidations();
    
    var makes = datass.getRange(1, 2, 1, datass.getLastColumn()).getValues(); // indices
    var makeIndex = makes[0].indexOf(e.getValue()) + 2; // +1 if found so that L18 works
    
    
    if (makeIndex != 0){
      
      var validationRange = datass.getRange(2, makeIndex, datass.getLastRow());
      var validationRule = SpreadsheetApp.newDataValidation().requireValueInRange(validationRange).build();
      e.offset(1, 0).setDataValidation(validationRule);
    }
   
  }
   
}
