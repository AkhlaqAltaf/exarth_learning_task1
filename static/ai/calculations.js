const reference_length = 283.598
const pixels_per_inch = 187.33

export function normolizer(p1, p2) {
  const dx = p1.x - p2.x;
  const dy = p1.y - p2.y;
  return Math.sqrt(dx * dx + dy * dy);
}


export function measurements(landmarks){
  const n = normolizer(landmarks[9],landmarks[13])
  return{
    hLength:handLength(landmarks[0] ,landmarks[12] ,n ),
    hTrigerLength:trigerLength(landmarks[5],landmarks[0],n),
    hGripLength : gripLength(landmarks[5],landmarks[17],n),


  }


}

function handLength(p1,p2,n){

  const dx = p1.x - p2.x;
  const dy = p1.y - p2.y;
  const distance = Math.sqrt(dx * dx + dy * dy);
  const _normal_distance = distance / n
  const _original_pixels = _normal_distance * reference_length
  const cm = _original_pixels / pixels_per_inch
  const  cm_per_inch = 2.54
  return cm / cm_per_inch



}

function trigerLength(p1,p2,n){

  const dx = p1.x - p2.x;
  const dy = p1.y - p2.y;
  const distance = Math.sqrt(dx * dx + dy * dy);
  const _normal_distance = distance / n
  const _original_pixels = _normal_distance * reference_length
  const cm = _original_pixels / pixels_per_inch
  const  cm_per_inch = 2.54
  return cm / cm_per_inch



}

function gripLength(p1,p2,n){

  const dx = p1.x - p2.x;
  const dy = p1.y - p2.y;
  const distance = Math.sqrt(dx * dx + dy * dy);
  const _normal_distance = distance / n
  const _original_pixels = _normal_distance * reference_length
  const cm = _original_pixels / pixels_per_inch
  const  cm_per_inch = 2.54
  return cm / cm_per_inch



}