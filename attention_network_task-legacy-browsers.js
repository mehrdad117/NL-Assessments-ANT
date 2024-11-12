/******************************* 
 * Attention_Network_Task *
 *******************************/


// store info about the experiment session:
let expName = 'attention_network_task';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.0039, 0.0039, 0.0039]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instrRoutineBegin());
flowScheduler.add(instrRoutineEachFrame());
flowScheduler.add(instrRoutineEnd());
flowScheduler.add(instr2RoutineBegin());
flowScheduler.add(instr2RoutineEachFrame());
flowScheduler.add(instr2RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);




const blocksLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(blocksLoopBegin(blocksLoopScheduler));
flowScheduler.add(blocksLoopScheduler);
flowScheduler.add(blocksLoopEnd);





flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'cond.xlsx', 'path': 'cond.xlsx'},
    {'name': 'stim/upper.png', 'path': 'stim/upper.png'},
    {'name': 'stim/congLeft.png', 'path': 'stim/congLeft.png'},
    {'name': 'stim/both.png', 'path': 'stim/both.png'},
    {'name': 'stim/centre.png', 'path': 'stim/centre.png'},
    {'name': 'stim/lower.png', 'path': 'stim/lower.png'},
    {'name': 'stim/congRight.png', 'path': 'stim/congRight.png'},
    {'name': 'stim/incongLeft.png', 'path': 'stim/incongLeft.png'},
    {'name': 'stim/incongRight.png', 'path': 'stim/incongRight.png'},
    {'name': 'cond-blocks.xlsx', 'path': 'cond-blocks.xlsx'},
    {'name': 'stim/upper.png', 'path': 'stim/upper.png'},
    {'name': 'stim/congLeft.png', 'path': 'stim/congLeft.png'},
    {'name': 'stim/both.png', 'path': 'stim/both.png'},
    {'name': 'stim/centre.png', 'path': 'stim/centre.png'},
    {'name': 'stim/blank.png', 'path': 'stim/blank.png'},
    {'name': 'stim/lower.png', 'path': 'stim/lower.png'},
    {'name': 'stim/congRight.png', 'path': 'stim/congRight.png'},
    {'name': 'stim/incongLeft.png', 'path': 'stim/incongLeft.png'},
    {'name': 'stim/incongRight.png', 'path': 'stim/incongRight.png'},
    {'name': 'stim/neutralLeft.png', 'path': 'stim/neutralLeft.png'},
    {'name': 'stim/neutralRight.png', 'path': 'stim/neutralRight.png'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'background.png', 'path': 'background.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var instrClock;
var startresp;
var inst1textbox;
var instr2Clock;
var startresp2;
var inst1textbox_2;
var fixationClock;
var durations;
var image;
var trial_counter_2;
var reminder;
var trialClock;
var text_fp1;
var cues;
var text_fp2;
var target;
var resp;
var fixationshort;
var trial_counter;
var reminder_2;
var feedbackClock;
var msg;
var correct_count;
var text;
var trial_counter_3;
var reminder_3;
var fix2Clock;
var image_2;
var trialsbClock;
var text_fp1_2;
var cues_2;
var text_fp2_2;
var target_2;
var resp_2;
var fixationshort_3;
var EndClock;
var background_6;
var inst1textbox_3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instr"
  instrClock = new util.Clock();
  startresp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  inst1textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'inst1textbox',
    text: 'به این آزمایش خوش آمدید.\n\nدر این آزمایش، یک فلش مرکزی به شما نمایش داده می\u200cشود که با فلش\u200cها یا بلوک\u200cهایی در اطرافش احاطه شده است. فلش مرکزی به سمت چپ یا راست اشاره می\u200cکند.\n\nگاهی فلش\u200cهای جانبی هم\u200cجهت با فلش مرکزی هستند و گاهی در جهت مخالف آن.\n\nبه عنوان مثال: >>>>> یا >><>>\n\nوظیفه\u200cی شما این است که به جهت فلش مرکزی پاسخ دهید.\n\nاگر فلش مرکزی به سمت راست اشاره می\u200cکند، کلید فلش راست را فشار دهید، و اگر به سمت چپ اشاره می\u200cکند، کلید فلش چپ را فشار دهید.\n\nبرای ادامه، کلید فاصله (space) را فشار دهید.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.1, 0.9],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "instr2"
  instr2Clock = new util.Clock();
  startresp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  inst1textbox_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'inst1textbox_2',
    text: 'در این وظیفه، شما باید با استفاده از کلیدهای جهت، به جهت فلش مرکزی پاسخ دهید.\n\nابتدا یک علامت به علاوه در مرکز صفحه نمایش داده می\u200cشود. این علامت گاهی با ظاهر شدن مربع\u200cهایی در صفحه همراه است که ممکن است محل هدف را نشان دهند یا ندهند. اگر مربع\u200cها بعد از علامت ظاهر شوند، به این معناست که هدف به زودی نمایش داده خواهد شد.\n\nاگر مربع\u200cها در بالا یا پایین علامت به علاوه ظاهر شوند، هدف به زودی در همان موقعیت نشان داده\u200cشده نمایان خواهد شد.\n\nانگشتان اشاره خود را روی کلیدهای جهت چپ و راست آماده کنید و برای شروع، کلید فاصله (space) را فشار دهید.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.1, 0.9],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  // Run 'Begin Experiment' code from fix_dur_code
  durations = [0.4, 0.45, 0.5, 0.55];
  
  image = new visual.TextStim({
    win: psychoJS.window,
    name: 'image',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  trial_counter_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'trial_counter_2',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.45)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  reminder = new visual.TextBox({
    win: psychoJS.window,
    name: 'reminder',
    text: 'به جهت فلش مرکزی با استفاده از کلیدهای چپ و راست روی صفحه\u200cکلید خود پاسخ دهید.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.4], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 0.2],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  text_fp1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fp1',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  cues = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cues', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  text_fp2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fp2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -2.0 
  });
  
  target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixationshort = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationshort',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  trial_counter = new visual.TextBox({
    win: psychoJS.window,
    name: 'trial_counter',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.45)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -6.0 
  });
  
  reminder_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'reminder_2',
    text: 'به جهت فلش مرکزی با استفاده از کلیدهای چپ و راست روی صفحه\u200cکلید خود پاسخ دهید.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.4], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 0.2],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -7.0 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  // Run 'Begin Experiment' code from fb_code
  msg = "";
  correct_count = 0;
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: undefined, ori: 0,
    languageStyle: 'Arabic',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  trial_counter_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'trial_counter_3',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.45)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.5, 0.1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -2.0 
  });
  
  reminder_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'reminder_3',
    text: 'به جهت فلش مرکزی با استفاده از کلیدهای چپ و راست روی صفحه\u200cکلید خود پاسخ دهید.',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0.4], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 0.2],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -3.0 
  });
  
  // Initialize components for Routine "fix2"
  fix2Clock = new util.Clock();
  // Run 'Begin Experiment' code from fix_dur_code_2
  durations = [0.4, 0.45, 0.5, 0.55];
  
  image_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'image_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trialsb"
  trialsbClock = new util.Clock();
  text_fp1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fp1_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  cues_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cues_2', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  text_fp2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_fp2_2',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -2.0 
  });
  
  target_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'target_2', units : 'height', 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 1.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  fixationshort_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixationshort_3',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  background_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'background_6', units : undefined, 
    image : 'background.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 1.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  inst1textbox_3 = new visual.TextBox({
    win: psychoJS.window,
    name: 'inst1textbox_3',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1.1, 0.9],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: 0.8,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: false,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var instrMaxDurationReached;
var _startresp_allKeys;
var instrMaxDuration;
var instrComponents;
function instrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instrClock.reset();
    routineTimer.reset();
    instrMaxDurationReached = false;
    // update component parameters for each repeat
    startresp.keys = undefined;
    startresp.rt = undefined;
    _startresp_allKeys = [];
    psychoJS.experiment.addData('instr.started', globalClock.getTime());
    instrMaxDuration = null
    // keep track of which components have finished
    instrComponents = [];
    instrComponents.push(startresp);
    instrComponents.push(inst1textbox);
    
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr' ---
    // get current time
    t = instrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *startresp* updates
    if (t >= 0.0 && startresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startresp.tStart = t;  // (not accounting for frame time here)
      startresp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startresp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startresp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startresp.clearEvents(); });
    }
    
    if (startresp.status === PsychoJS.Status.STARTED) {
      let theseKeys = startresp.getKeys({keyList: ['space'], waitRelease: false});
      _startresp_allKeys = _startresp_allKeys.concat(theseKeys);
      if (_startresp_allKeys.length > 0) {
        startresp.keys = _startresp_allKeys[_startresp_allKeys.length - 1].name;  // just the last key pressed
        startresp.rt = _startresp_allKeys[_startresp_allKeys.length - 1].rt;
        startresp.duration = _startresp_allKeys[_startresp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *inst1textbox* updates
    if (t >= 0.0 && inst1textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst1textbox.tStart = t;  // (not accounting for frame time here)
      inst1textbox.frameNStart = frameN;  // exact frame index
      
      inst1textbox.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr' ---
    instrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr.stopped', globalClock.getTime());
    startresp.stop();
    // the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instr2MaxDurationReached;
var _startresp2_allKeys;
var instr2MaxDuration;
var instr2Components;
function instr2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instr2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instr2Clock.reset();
    routineTimer.reset();
    instr2MaxDurationReached = false;
    // update component parameters for each repeat
    startresp2.keys = undefined;
    startresp2.rt = undefined;
    _startresp2_allKeys = [];
    psychoJS.experiment.addData('instr2.started', globalClock.getTime());
    instr2MaxDuration = null
    // keep track of which components have finished
    instr2Components = [];
    instr2Components.push(startresp2);
    instr2Components.push(inst1textbox_2);
    
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instr2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instr2' ---
    // get current time
    t = instr2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *startresp2* updates
    if (t >= 0.0 && startresp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startresp2.tStart = t;  // (not accounting for frame time here)
      startresp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startresp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startresp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startresp2.clearEvents(); });
    }
    
    if (startresp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = startresp2.getKeys({keyList: ['space'], waitRelease: false});
      _startresp2_allKeys = _startresp2_allKeys.concat(theseKeys);
      if (_startresp2_allKeys.length > 0) {
        startresp2.keys = _startresp2_allKeys[_startresp2_allKeys.length - 1].name;  // just the last key pressed
        startresp2.rt = _startresp2_allKeys[_startresp2_allKeys.length - 1].rt;
        startresp2.duration = _startresp2_allKeys[_startresp2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *inst1textbox_2* updates
    if (t >= 0.0 && inst1textbox_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst1textbox_2.tStart = t;  // (not accounting for frame time here)
      inst1textbox_2.frameNStart = frameN;  // exact frame index
      
      inst1textbox_2.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instr2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instr2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instr2' ---
    instr2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instr2.stopped', globalClock.getTime());
    startresp2.stop();
    // the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(fixationRoutineEachFrame());
      trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var blocks;
function blocksLoopBegin(blocksLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    blocks = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'blocks'
    });
    psychoJS.experiment.addLoop(blocks); // add the loop to the experiment
    currentLoop = blocks;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    blocks.forEach(function() {
      snapshot = blocks.getSnapshot();
    
      blocksLoopScheduler.add(importConditions(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      blocksLoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      blocksLoopScheduler.add(trials_2LoopScheduler);
      blocksLoopScheduler.add(trials_2LoopEnd);
      blocksLoopScheduler.add(blocksLoopEndIteration(blocksLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'cond-blocks.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(fix2RoutineBegin(snapshot));
      trials_2LoopScheduler.add(fix2RoutineEachFrame());
      trials_2LoopScheduler.add(fix2RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trialsbRoutineBegin(snapshot));
      trials_2LoopScheduler.add(trialsbRoutineEachFrame());
      trials_2LoopScheduler.add(trialsbRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function blocksLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(blocks);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function blocksLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fixationMaxDurationReached;
var fixDuration;
var fixationMaxDuration;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    fixationClock.reset();
    routineTimer.reset();
    fixationMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fix_dur_code
    util.shuffle(durations);
    fixDuration = durations[0];
    
    image.setText('+');
    trial_counter_2.setText((((trials.thisN + 1).toString() + "/") + trials.nTotal.toString()));
    psychoJS.experiment.addData('fixation.started', globalClock.getTime());
    fixationMaxDuration = null
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(image);
    fixationComponents.push(trial_counter_2);
    fixationComponents.push(reminder);
    
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation' ---
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    
    // *trial_counter_2* updates
    if (t >= 0.0 && trial_counter_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_counter_2.tStart = t;  // (not accounting for frame time here)
      trial_counter_2.frameNStart = frameN;  // exact frame index
      
      trial_counter_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (trial_counter_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_counter_2.setAutoDraw(false);
    }
    
    
    // *reminder* updates
    if (t >= 0.0 && reminder.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder.tStart = t;  // (not accounting for frame time here)
      reminder.frameNStart = frameN;  // exact frame index
      
      reminder.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (reminder.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reminder.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation' ---
    fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fixation.stopped', globalClock.getTime());
    // the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialMaxDurationReached;
var _resp_allKeys;
var trialMaxDuration;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trialClock.reset(routineTimer.getTime());
    routineTimer.add(2.200000);
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    cues.setImage(cue);
    target.setOri(targOrientation);
    target.setImage(tar);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    trial_counter.setText((((trials.thisN + 1).toString() + "/") + trials.nTotal.toString()));
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(text_fp1);
    trialComponents.push(cues);
    trialComponents.push(text_fp2);
    trialComponents.push(target);
    trialComponents.push(resp);
    trialComponents.push(fixationshort);
    trialComponents.push(trial_counter);
    trialComponents.push(reminder_2);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fp1* updates
    if (t >= 0.0 && text_fp1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fp1.tStart = t;  // (not accounting for frame time here)
      text_fp1.frameNStart = frameN;  // exact frame index
      
      text_fp1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_fp1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fp1.setAutoDraw(false);
    }
    
    
    // *cues* updates
    if (t >= 0 && cues.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cues.tStart = t;  // (not accounting for frame time here)
      cues.frameNStart = frameN;  // exact frame index
      
      cues.setAutoDraw(true);
    }
    
    frameRemains = 0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (cues.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cues.setAutoDraw(false);
    }
    
    
    // *text_fp2* updates
    if (t >= 0.1 && text_fp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fp2.tStart = t;  // (not accounting for frame time here)
      text_fp2.frameNStart = frameN;  // exact frame index
      
      text_fp2.setAutoDraw(true);
    }
    
    frameRemains = 0.1 + 2.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_fp2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fp2.setAutoDraw(false);
    }
    
    
    // *target* updates
    if (t >= 0.5 && target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target.tStart = t;  // (not accounting for frame time here)
      target.frameNStart = frameN;  // exact frame index
      
      target.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target.setAutoDraw(false);
    }
    
    
    // *resp* updates
    if (t >= 0.5 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }
    
    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[0].name;  // just the first key pressed
        resp.rt = _resp_allKeys[0].rt;
        resp.duration = _resp_allKeys[0].duration;
        // was this correct?
        if (resp.keys == corrAns) {
            resp.corr = 1;
        } else {
            resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixationshort* updates
    if (t >= 0.0 && fixationshort.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationshort.tStart = t;  // (not accounting for frame time here)
      fixationshort.frameNStart = frameN;  // exact frame index
      
      fixationshort.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixationshort.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationshort.setAutoDraw(false);
    }
    
    
    // *trial_counter* updates
    if (t >= 0.0 && trial_counter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_counter.tStart = t;  // (not accounting for frame time here)
      trial_counter.frameNStart = frameN;  // exact frame index
      
      trial_counter.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (trial_counter.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_counter.setAutoDraw(false);
    }
    
    
    // *reminder_2* updates
    if (t >= 0.0 && reminder_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_2.tStart = t;  // (not accounting for frame time here)
      reminder_2.frameNStart = frameN;  // exact frame index
      
      reminder_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (reminder_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reminder_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         resp.corr = 1;  // correct non-response
      } else {
         resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp.corr, level);
    }
    psychoJS.experiment.addData('resp.keys', resp.keys);
    psychoJS.experiment.addData('resp.corr', resp.corr);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        psychoJS.experiment.addData('resp.duration', resp.duration);
        routineTimer.reset();
        }
    
    resp.stop();
    if (trialMaxDurationReached) {
        trialClock.add(trialMaxDuration);
    } else {
        trialClock.add(2.200000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackMaxDurationReached;
var fbcol;
var feedbackMaxDuration;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedbackClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fb_code
    msg = "\u0627\u0634\u062a\u0628\u0627\u0647!";
    fbcol = "black";
    if (resp.corr) {
        msg = (("\u0635\u062d\u06cc\u062d \u0633\u0631\u0639\u062a \u067e\u0627\u0633\u062e \u0634\u0645\u0627: " + Number.parseInt((resp.rt * 1000)).toString()) + "ms");
        correct_count += 1;
        fbcol = "green";
    } else {
        if ((! resp.keys)) {
            msg = "\u067e\u0627\u0633\u062e \u0641\u0631\u0627\u0645\u0648\u0634 \u0646\u0634\u0648\u062f";
        }
    }
    
    text.setColor(new util.Color(fbcol));
    text.setText(msg);
    trial_counter_3.setText((((trials.thisN + 1).toString() + "/") + trials.nTotal.toString()));
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    feedbackMaxDuration = null
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(text);
    feedbackComponents.push(trial_counter_3);
    feedbackComponents.push(reminder_3);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    
    // *trial_counter_3* updates
    if (t >= 0.0 && trial_counter_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_counter_3.tStart = t;  // (not accounting for frame time here)
      trial_counter_3.frameNStart = frameN;  // exact frame index
      
      trial_counter_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (trial_counter_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_counter_3.setAutoDraw(false);
    }
    
    
    // *reminder_3* updates
    if (t >= 0.0 && reminder_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      reminder_3.tStart = t;  // (not accounting for frame time here)
      reminder_3.frameNStart = frameN;  // exact frame index
      
      reminder_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (reminder_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      reminder_3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    if (feedbackMaxDurationReached) {
        feedbackClock.add(feedbackMaxDuration);
    } else {
        feedbackClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var fix2MaxDurationReached;
var fix2MaxDuration;
var fix2Components;
function fix2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fix2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    fix2Clock.reset();
    routineTimer.reset();
    fix2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from fix_dur_code_2
    util.shuffle(durations);
    fixDuration = durations[0];
    
    image_2.setText('+');
    psychoJS.experiment.addData('fix2.started', globalClock.getTime());
    fix2MaxDuration = null
    // keep track of which components have finished
    fix2Components = [];
    fix2Components.push(image_2);
    
    fix2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function fix2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fix2' ---
    // get current time
    t = fix2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + fixDuration - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    fix2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fix2' ---
    fix2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('fix2.stopped', globalClock.getTime());
    // Run 'End Routine' code from fix_dur_code_2
    psychoJS.experiment.addData("fixDuration", fixDuration);
    
    // the Routine "fix2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialsbMaxDurationReached;
var _resp_2_allKeys;
var trialsbMaxDuration;
var trialsbComponents;
function trialsbRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trialsb' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trialsbClock.reset(routineTimer.getTime());
    routineTimer.add(2.200000);
    trialsbMaxDurationReached = false;
    // update component parameters for each repeat
    cues_2.setImage(cue);
    target_2.setOri(targOrientation);
    target_2.setImage(tar);
    resp_2.keys = undefined;
    resp_2.rt = undefined;
    _resp_2_allKeys = [];
    psychoJS.experiment.addData('trialsb.started', globalClock.getTime());
    trialsbMaxDuration = null
    // keep track of which components have finished
    trialsbComponents = [];
    trialsbComponents.push(text_fp1_2);
    trialsbComponents.push(cues_2);
    trialsbComponents.push(text_fp2_2);
    trialsbComponents.push(target_2);
    trialsbComponents.push(resp_2);
    trialsbComponents.push(fixationshort_3);
    
    trialsbComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialsbRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trialsb' ---
    // get current time
    t = trialsbClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_fp1_2* updates
    if (t >= 0.0 && text_fp1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fp1_2.tStart = t;  // (not accounting for frame time here)
      text_fp1_2.frameNStart = frameN;  // exact frame index
      
      text_fp1_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_fp1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fp1_2.setAutoDraw(false);
    }
    
    
    // *cues_2* updates
    if (t >= 0 && cues_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cues_2.tStart = t;  // (not accounting for frame time here)
      cues_2.frameNStart = frameN;  // exact frame index
      
      cues_2.setAutoDraw(true);
    }
    
    frameRemains = 0 + 0.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (cues_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cues_2.setAutoDraw(false);
    }
    
    
    // *text_fp2_2* updates
    if (t >= 0.1 && text_fp2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_fp2_2.tStart = t;  // (not accounting for frame time here)
      text_fp2_2.frameNStart = frameN;  // exact frame index
      
      text_fp2_2.setAutoDraw(true);
    }
    
    frameRemains = 0.1 + 2.1 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_fp2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_fp2_2.setAutoDraw(false);
    }
    
    
    // *target_2* updates
    if (t >= 0.5 && target_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target_2.tStart = t;  // (not accounting for frame time here)
      target_2.frameNStart = frameN;  // exact frame index
      
      target_2.setAutoDraw(true);
    }
    
    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (target_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      target_2.setAutoDraw(false);
    }
    
    
    // *resp_2* updates
    if (t >= 0.5 && resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp_2.tStart = t;  // (not accounting for frame time here)
      resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp_2.clearEvents(); });
    }
    
    frameRemains = 0.5 + 1.7 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp_2.status = PsychoJS.Status.FINISHED;
        }
      
    if (resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp_2.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_2_allKeys = _resp_2_allKeys.concat(theseKeys);
      if (_resp_2_allKeys.length > 0) {
        resp_2.keys = _resp_2_allKeys[0].name;  // just the first key pressed
        resp_2.rt = _resp_2_allKeys[0].rt;
        resp_2.duration = _resp_2_allKeys[0].duration;
        // was this correct?
        if (resp_2.keys == corrAns) {
            resp_2.corr = 1;
        } else {
            resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *fixationshort_3* updates
    if (t >= 0.0 && fixationshort_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationshort_3.tStart = t;  // (not accounting for frame time here)
      fixationshort_3.frameNStart = frameN;  // exact frame index
      
      fixationshort_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixationshort_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationshort_3.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialsbComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialsbRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trialsb' ---
    trialsbComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trialsb.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (resp_2.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         resp_2.corr = 1;  // correct non-response
      } else {
         resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp_2.corr, level);
    }
    psychoJS.experiment.addData('resp_2.keys', resp_2.keys);
    psychoJS.experiment.addData('resp_2.corr', resp_2.corr);
    if (typeof resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp_2.rt', resp_2.rt);
        psychoJS.experiment.addData('resp_2.duration', resp_2.duration);
        routineTimer.reset();
        }
    
    resp_2.stop();
    if (trialsbMaxDurationReached) {
        trialsbClock.add(trialsbMaxDuration);
    } else {
        trialsbClock.add(2.200000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var EndMaxDurationReached;
var EndMaxDuration;
var EndComponents;
function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'End' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    EndClock.reset();
    routineTimer.reset();
    EndMaxDurationReached = false;
    // update component parameters for each repeat
    inst1textbox_3.setText('لطفا تا ذخیره نتایج صبر کنید...');
    // Disable downloading results to browser
    psychoJS._saveResults = 0; 
    
    // Generate filename for results
    let filename = psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime + '.csv';
    
    // Extract data object from experiment
    let dataObj = psychoJS._experiment._trialsData;
    
    // Convert data object to CSV
    let data = [Object.keys(dataObj[0])].concat(dataObj).map(it => {
        return Object.values(it).toString()
    }).join('\n')
    
    // Send data to OSF via DataPipe
    console.log('Saving data...');
    fetch('https://pipe.jspsych.org/api/data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Accept: '*/*',
        },
        body: JSON.stringify({
            experimentID: 'VgIiMiyNwW6P', // ⭑ UPDATE WITH YOUR DATAPIPE EXPERIMENT ID ⭑
            filename: filename,
            data: data,
        }),
    }).then(response => response.json()).then(data => {
        // Log response and force experiment end
        console.log(data);
        quitPsychoJS();
    })
    psychoJS.experiment.addData('End.started', globalClock.getTime());
    EndMaxDuration = null
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(background_6);
    EndComponents.push(inst1textbox_3);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'End' ---
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *background_6* updates
    if (t >= 0.0 && background_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      background_6.tStart = t;  // (not accounting for frame time here)
      background_6.frameNStart = frameN;  // exact frame index
      
      background_6.setAutoDraw(true);
    }
    
    
    // *inst1textbox_3* updates
    if (t >= 0.0 && inst1textbox_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inst1textbox_3.tStart = t;  // (not accounting for frame time here)
      inst1textbox_3.frameNStart = frameN;  // exact frame index
      
      inst1textbox_3.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'End' ---
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('End.stopped', globalClock.getTime());
    // the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
