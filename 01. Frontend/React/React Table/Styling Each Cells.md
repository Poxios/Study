# 테이블의 각 행, 열마다 스타일링하기

- headless 라이브러리인 react-table 특성상, 사용자가 굉장히 많은 것들을 자유롭게 수행할 수 있다.
- `getCellProps()` 메소드와 별개로, 사용자가 `getCellStyles(cellProps)`와 같은 메소드를 정의해서 `cellProps.column.id`, `cellProps.row.values`와 같이 해당 cell의 정보들을 가지고 상황에 맞는 inline style을 return 시켜줄 수 있다. 참고로 inline style은 성능과 크게 상관이 없다.

## 예시

```JSX
// ...table.tsx 아무데나
const borderRightCell = ["requestDate", "userName"];
const getCellStyle = (cellProps) => {
  if (borderRightCell.find(cellProps.column.id)) {
    return {
      style: {
        borderRight: "1px solid black",
      },
    };
  }
};

// ...Table Rendering 내부
// ...
 </TableHead>
<TableBody>
    {table.page.map((row, rowIndex) => {
        table.prepareRow(row);
        return (
        <TableRow {...row.getRowProps()}>
            {row.cells.map((cell) => {
            return (
                <TableCell
                {...{ ...cell.getCellProps(), ...getCellStyle(cell) }}>
                {cell.render("Cell")}
                </TableCell>
            );
            })}
        </TableRow>
        );
    })}
</TableBody>
```
