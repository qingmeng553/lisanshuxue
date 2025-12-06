// 五种性质判定
export function isReflexive(m)   { const n=m.length; for(let i=0;i<n;i++) if(m[i][i]!==1) return false; return true }
export function isIrreflexive(m) { const n=m.length; for(let i=0;i<n;i++) if(m[i][i]!==0) return false; return true }
export function isSymmetric(m)   { const n=m.length; for(let i=0;i<n;i++) for(let j=0;j<n;j++) if(m[i][j]!==m[j][i]) return false; return true }
export function isAntiSymmetric(m){ const n=m.length; for(let i=0;i<n;i++) for(let j=0;j<n;j++) if(i!==j && m[i][j]===1 && m[j][i]===1) return false; return true }
export function isTransitive(m)  { const n=m.length; for(let i=0;i<n;i++) for(let j=0;j<n;j++) if(m[i][j]===1) for(let k=0;k<n;k++) if(m[j][k]===1 && m[i][k]!==1) return false; return true }

// 闭包
export function reflexiveClosure(m)  { const c=m.map(r=>r.slice()); for(let i=0;i<c.length;i++) c[i][i]=1; return c }
export function symmetricClosure(m)  { const c=m.map(r=>r.slice()); for(let i=0;i<c.length;i++) for(let j=0;j<c.length;j++) if(c[i][j]===1) c[j][i]=1; return c }
export function transitiveClosure(m) { const c=m.map(r=>r.slice()), n=c.length; for(let k=0;k<n;k++) for(let i=0;i<n;i++) for(let j=0;j<n;j++) if(c[i][k]&&c[k][j]) c[i][j]=1; return c }

// Warshall 逐步记录（用于演示）
export function warshallSteps(m){
  const R = m.map(r=>r.slice()), n=R.length, steps=[JSON.parse(JSON.stringify(R))]
  for(let k=0;k<n;k++){
    for(let i=0;i<n;i++){
      for(let j=0;j<n;j++){
        R[i][j] = R[i][j] || (R[i][k] && R[k][j])
      }
    }
    steps.push(JSON.parse(JSON.stringify(R)))
  }
  return steps
}